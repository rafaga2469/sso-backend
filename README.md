# SSO Backend

Este proyecto es una API sencilla de autenticación implementada con **Django** y **Django REST Framework**. Proporciona un mecanismo de inicio de sesión, registro de usuarios y obtención de tokens JWT empleando `rest_framework_simplejwt`. También incluye soporte CORS para permitir peticiones desde un cliente front‑end.

## Requisitos

- Python 3.10 o superior
- Las dependencias de Python listadas en `requirements.txt`

## Instalación

1. Crear un entorno virtual y activarlo:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Copiar el archivo `.env.example` a `.env` y ajustar los valores sensibles:

   ```bash
   cp .env.example .env
   # editar .env para ajustar SECRET_KEY y otras opciones
   ```

4. Aplicar migraciones y ejecutar el servidor de desarrollo:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Endpoints principales

- `POST /sso/token/cookie/` — inicio de sesión, devuelve el token de acceso y guarda el token de refresco en una cookie.
- `POST /sso/token/refresh/` — renueva el token de acceso utilizando la cookie de refresco.
- `POST /sso/logout/` — cierra la sesión eliminando la cookie de refresco.
- `GET /sso/me/` — devuelve información del usuario autenticado.
- `POST /sso/register/` — crea un nuevo usuario.

Todos los endpoints anteriores se definen en el módulo `sso`.

## Desarrollo

El archivo `sso_backend/settings.py` configura `rest_framework_simplejwt` y `django-cors-headers`. Revisa este archivo si necesitas modificar tiempos de expiración de los tokens o el origen permitido de CORS.

## Licencia

Este proyecto se distribuye bajo los términos de la licencia MIT.
