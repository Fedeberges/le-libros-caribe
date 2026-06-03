# Guía de Deploy — Le Libros Caribe

## Paso 1: GitHub (gratis)
1. Ve a https://github.com y crea una cuenta
2. Crea un repositorio nuevo llamado `le-libros-caribe` (público)
3. En tu computadora, abre PowerShell en la carpeta del proyecto:
   ```
   cd "C:\Users\feder\OneDrive\Desktop\pa claude\le-libros-caribe"
   git init
   git add .
   git commit -m "primer commit"
   git remote add origin https://github.com/TU_USUARIO/le-libros-caribe.git
   git push -u origin main
   ```

## Paso 2: Base de datos — Supabase (gratis)
1. Ve a https://supabase.com → "Start for free"
2. Crea un proyecto → ponle nombre "le-libros-caribe"
3. Ve a Settings → Database → Connection string → URI
4. Copia esa URL (empieza con `postgresql://...`)
5. Guárdala — la necesitas en el Paso 3

## Paso 3: Backend — Render (gratis)
1. Ve a https://render.com → "Get Started for Free"
2. Conecta tu cuenta de GitHub
3. New → Web Service → selecciona tu repo `le-libros-caribe`
4. Configura:
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. En Environment Variables agrega:
   - `DATABASE_URL` = la URL de Supabase del paso 2
   - `SECRET_KEY` = cualquier string largo y aleatorio
6. Deploy → espera ~3 minutos
7. Copia la URL que te da Render (ej: `https://le-libros-caribe-api.onrender.com`)

## Paso 4: Actualizar URL del API en el frontend
Abre `frontend/index.html` y reemplaza `le-libros-caribe-api.onrender.com`
con la URL real que te dio Render en el paso 3.

## Paso 5: Frontend — Netlify (gratis)
1. Ve a https://netlify.com → "Sign up"
2. Arrastra y suelta la carpeta `frontend/` en el dashboard de Netlify
3. ¡Listo! Te da una URL tipo `https://amazing-name-123.netlify.app`

## Paso 6: Dominio (opcional, ~$10-15/año)
1. Ve a https://namecheap.com
2. Busca `lelibrosexample.com` (o el nombre que quieras)
3. Cómpralo
4. En Netlify: Domain settings → Add custom domain → sigue las instrucciones
5. En Namecheap: apunta los nameservers a los de Netlify

## Paso 7: Cargar libros en producción
Una vez el backend esté en Render, abre la terminal y ejecuta:
```
DATABASE_URL="tu-url-de-supabase" python -m services.gutenberg
```
O conéctate al shell de Render y córrelo ahí.
