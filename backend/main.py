from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from database import engine
import models
from routes import auth, books, subscriptions

# Crear tablas si no existen
models.Base.metadata.create_all(bind=engine)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Le Libros Caribe API",
    description="API para la plataforma de libros de dominio público del Caribe",
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS — en producción, reemplaza "*" por tu dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(subscriptions.router)

@app.get("/")
def root():
    return {"message": "Le Libros Caribe API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}
