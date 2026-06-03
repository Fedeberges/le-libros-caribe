"""
Servicio de ingesta de libros desde Project Gutenberg.
Ejecutar manualmente: python -m services.gutenberg
O programar con cron para correr noche a noche.
"""
import httpx
import json
from sqlalchemy.orm import Session
from database import SessionLocal
from config import settings
import models

GUTENBERG_API = "https://gutendex.com/books/"

def build_amazon_url(title: str, author: str) -> str:
    query = f"{title} {author}".replace(" ", "+")
    return f"https://www.amazon.com/s?k={query}&tag={settings.AMAZON_AFFILIATE_TAG}"

def ingest_page(page: int, db: Session) -> int:
    """Ingesta una página del catálogo de Gutenberg. Retorna cantidad de libros procesados."""
    response = httpx.get(GUTENBERG_API, params={"page": page}, timeout=30)
    response.raise_for_status()
    data = response.json()
    count = 0
    for item in data.get("results", []):
        external_id = f"gutenberg-{item['id']}"
        if db.query(models.Book).filter_by(external_id=external_id).first():
            continue  # ya existe
        authors = ", ".join(a["name"] for a in item.get("authors", []))
        subjects = ", ".join(item.get("subjects", [])[:3])
        formats = item.get("formats", {})
        cover = formats.get("image/jpeg", "")
        epub = formats.get("application/epub+zip", "")
        book = models.Book(
            external_id=external_id,
            source="gutenberg",
            title=item["title"],
            author=authors,
            language=item.get("languages", ["en"])[0],
            subject=subjects,
            cover_url=cover,
            file_url=epub,
            amazon_url=build_amazon_url(item["title"], authors),
        )
        db.add(book)
        count += 1
    db.commit()
    return count

def run_ingestion(max_pages: int = 50):
    db = SessionLocal()
    try:
        total = 0
        for page in range(1, max_pages + 1):
            n = ingest_page(page, db)
            total += n
            print(f"Página {page}: {n} libros nuevos (total: {total})")
            if n == 0:
                break
        print(f"Ingesta completada. Total libros nuevos: {total}")
    finally:
        db.close()

if __name__ == "__main__":
    run_ingestion()
