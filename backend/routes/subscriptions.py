from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from security import get_current_user
from config import settings
import models
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

@router.post("/checkout")
def create_checkout(db: Session = Depends(get_db), user=Depends(get_current_user)):
    """Crea sesión de pago en Stripe para suscripción premium."""
    session = stripe.checkout.Session.create(
        customer_email=user.email,
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{"price": settings.STRIPE_PRICE_ID_PREMIUM, "quantity": 1}],
        success_url="http://localhost:4200/subscription/success",
        cancel_url="http://localhost:4200/subscription/cancel",
        metadata={"user_id": str(user.id)},
    )
    return {"checkout_url": session.url}

@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    """Webhook de Stripe — actualiza suscripción tras pago exitoso."""
    payload = await request.body()
    sig = request.headers.get("stripe-signature")
    try:
        event = stripe.Webhook.construct_event(payload, sig, settings.STRIPE_WEBHOOK_SECRET)
    except Exception:
        raise HTTPException(status_code=400, detail="Webhook inválido")

    if event["type"] == "checkout.session.completed":
        user_id = int(event["data"]["object"]["metadata"]["user_id"])
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            user.subscription_tier = models.SubscriptionTier.PREMIUM
            user.stripe_customer_id = event["data"]["object"]["customer"]
            db.commit()

    return {"status": "ok"}

@router.delete("/cancel")
def cancel_subscription(db: Session = Depends(get_db), user=Depends(get_current_user)):
    """Cancela la suscripción del usuario."""
    if not user.stripe_customer_id:
        raise HTTPException(status_code=400, detail="No tienes suscripción activa")
    subscriptions = stripe.Subscription.list(customer=user.stripe_customer_id, status="active")
    for sub in subscriptions.auto_paging_iter():
        stripe.Subscription.cancel(sub.id)
    user.subscription_tier = models.SubscriptionTier.FREE
    db.commit()
    return {"message": "Suscripción cancelada"}
