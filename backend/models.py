from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum

class SubscriptionTier(str, enum.Enum):
    FREE = "free"
    PREMIUM = "premium"
    API = "api"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    subscription_tier = Column(Enum(SubscriptionTier), default=SubscriptionTier.FREE)
    stripe_customer_id = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    library = relationship("UserLibrary", back_populates="user")
    annotations = relationship("Annotation", back_populates="user")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String(100), unique=True, index=True)  # ej: gutenberg-1342
    source = Column(String(50), nullable=False)                 # gutenberg, openlibrary, etc.
    title = Column(String(500), nullable=False)
    author = Column(String(500))
    language = Column(String(10), default="en")
    subject = Column(String(500))
    description = Column(Text)
    cover_url = Column(String(500))
    file_url = Column(String(500))          # EPUB/PDF en S3
    amazon_url = Column(String(500))        # enlace afiliado
    download_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserLibrary(Base):
    __tablename__ = "user_library"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    added_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="library")
    book = relationship("Book")

class Annotation(Base):
    __tablename__ = "annotations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    text = Column(Text, nullable=False)
    position = Column(String(100))          # referencia de posición en el libro
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="annotations")
