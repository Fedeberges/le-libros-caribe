# 📚 Le Libros Caribe

Plataforma web para descubrir, leer y organizar libros de dominio público y licencias Creative Commons.

## Stack tecnológico
- **Frontend:** Angular 17
- **Backend:** Python 3.11 + FastAPI
- **Base de datos:** PostgreSQL 15
- **Caché:** Redis
- **Almacenamiento:** AWS S3 (o compatible)
- **Pagos:** Stripe

## Estructura del proyecto

```
le-libros-caribe/
├── backend/          # API REST con FastAPI
├── frontend/         # App Angular
├── database/         # Schema SQL
└── docker-compose.yml
```

## Inicio rápido

### Requisitos
- Docker + Docker Compose
- Node.js 18+
- Python 3.11+

### Levantar con Docker
```bash
docker-compose up -d
```

### Backend (manual)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
API disponible en: http://localhost:8000
Documentación: http://localhost:8000/docs

### Frontend (manual)
```bash
cd frontend
npm install
ng serve
```
App disponible en: http://localhost:4200

## Variables de entorno (backend/.env)
```
DATABASE_URL=postgresql://user:password@localhost/le_libros_caribe
SECRET_KEY=tu-clave-secreta-muy-larga
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PRICE_ID=price_...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
S3_BUCKET_NAME=le-libros-caribe
REDIS_URL=redis://localhost:6379
```

## Monetización implementada
1. Afiliados Amazon (enlace por libro)
2. Suscripción premium vía Stripe
3. Publicidad (Google AdSense ready)
4. API de acceso para terceros (tier API)
5. Print-on-demand (integración Lulu)

## Fuentes de libros
- Project Gutenberg
- Standard Ebooks
- Open Library (Internet Archive)
- Feedbooks
