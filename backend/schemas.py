from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from models import SubscriptionTier

# Auth
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str]
    subscription_tier: SubscriptionTier
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Books
class BookOut(BaseModel):
    id: int
    external_id: str
    source: str
    title: str
    author: Optional[str]
    language: Optional[str]
    subject: Optional[str]
    description: Optional[str]
    cover_url: Optional[str]
    amazon_url: Optional[str]
    download_count: int
    class Config:
        from_attributes = True

class BookList(BaseModel):
    total: int
    page: int
    per_page: int
    books: list[BookOut]

# Annotations
class AnnotationCreate(BaseModel):
    book_id: int
    text: str
    position: Optional[str] = None

class AnnotationOut(BaseModel):
    id: int
    book_id: int
    text: str
    position: Optional[str]
    created_at: datetime
    class Config:
        from_attributes = True
