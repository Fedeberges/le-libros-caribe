# Cómo arrancar Le Libros Caribe

## Paso 1 — Backend (API)

Abre una terminal (CMD o PowerShell) y pega esto:

```
cd "C:\Users\feder\OneDrive\Desktop\pa claude\le-libros-caribe\backend"
pip install -r requirements.txt
uvicorn main:app --reload
```

✅ Cuando veas `Uvicorn running on http://127.0.0.1:8000` — el backend está listo.

---

## Paso 2 — Frontend (app web)

Abre **otra** terminal (sin cerrar la anterior) y pega:

```
cd "C:\Users\feder\OneDrive\Desktop\pa claude\le-libros-caribe\frontend"
npm install -g @angular/cli
npm install
ng serve
```

✅ Cuando veas `Local: http://localhost:4200/` — abre el browser y entra a esa URL.

---

## Paso 3 — Cargar libros (opcional)

Abre **otra** terminal con el backend corriendo y ejecuta:

```
cd "C:\Users\feder\OneDrive\Desktop\pa claude\le-libros-caribe\backend"
python -m services.gutenberg
```

Esto descarga miles de libros de Project Gutenberg a la base de datos.

---

## Requisitos previos
- Python instalado → https://python.org/downloads
- Node.js instalado → https://nodejs.org
