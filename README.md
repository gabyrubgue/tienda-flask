# Tienda Template (Flask + HTML/CSS/JS + Tailwind via CDN)

**Contenido:** Aplicación minimal que corre con Flask y una SPA frontend en `templates/index.html`. La mayoría de la lógica (productos, carrito, auth demo, configuración) está en `static/js/app.js` y se persiste en `localStorage`.

## Requisitos
- Python 3.8+
- pip

## Instalación y ejecución
1. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate   # Windows
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la app:
   ```bash
   python app.py
   ```
   Abre: http://localhost:5000

## Configurar Firebase (opcional)
- Crea un proyecto en https://console.firebase.google.com
- Habilita Authentication -> Sign-in providers: Google y Facebook
- Copia las credenciales y pégalas en `.env` o usa el archivo `.env.sample` como guía.
- En el código cliente (`templates/index.html` and `static/js/app.js`) hay marcas `AQUI PEGAR FIREBASE CONFIG` indicando dónde agregar.

## Características implementadas (cliente)
- Header editable (inline) + logo upload con preview
- Menú responsive con hamburger
- Login demo y placeholders para Firebase Auth (Google, Facebook)
- Página de productos: list, add product form, checkbox permitir cantidad, persistencia en localStorage
- Export/Import JSON de productos
- Carrito (modal) con editar cantidades, subtotal y total, limpiar carrito y checkout simulado
- Páginas Servicios y Contacto con editor simple y formulario de contacto que escribe en consola
- Footer editable con persistencia en localStorage
- Panel admin lateral: editar nombre/logo/menu, export/import config JSON
- Tecla ESC cierra modal (global)

## Notas
- No se incluye ninguna clave real.
- Tailwind se carga vía CDN para evitar pasos de build y hacer la plantilla fácil de usar.
- Para producción se recomienda compilar assets y usar hosting adecuado.
