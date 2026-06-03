from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from schemas import BookOut, BookList
from security import get_current_user, require_premium
import models

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=BookList)
def list_books(
    q: str = Query(None, description="Búsqueda por título o autor"),
    language: str = Query(None),
    subject: str = Query(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(models.Book)
    if q:
        query = query.filter(
            models.Book.title.ilike(f"%{q}%") | models.Book.author.ilike(f"%{q}%")
        )
    if language:
        query = query.filter(models.Book.language == language)
    if subject:
        query = query.filter(models.Book.subject.ilike(f"%{subject}%"))

    total = query.count()
    books = query.order_by(models.Book.title).offset((page - 1) * per_page).limit(per_page).all()
    return {"total": total, "page": page, "per_page": per_page, "books": books}

@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return book

@router.post("/{book_id}/library")
def add_to_library(book_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    existing = db.query(models.UserLibrary).filter_by(user_id=user.id, book_id=book_id).first()
    if existing:
        return {"message": "Ya está en tu biblioteca"}
    entry = models.UserLibrary(user_id=user.id, book_id=book_id)
    db.add(entry)
    db.commit()
    return {"message": "Agregado a tu biblioteca"}

@router.get("/my/library", response_model=list[BookOut])
def my_library(db: Session = Depends(get_db), user=Depends(get_current_user)):
    entries = db.query(models.UserLibrary).filter_by(user_id=user.id).all()
    return [e.book for e in entries]

@router.post("/{book_id}/annotations")
def add_annotation(book_id: int, text: str, position: str = None,
                   db: Session = Depends(get_db), user=Depends(require_premium)):
    annotation = models.Annotation(user_id=user.id, book_id=book_id, text=text, position=position)
    db.add(annotation)
    db.commit()
    return {"message": "Anotación guardada"}
