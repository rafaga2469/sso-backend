# SSO Backend

Este proyecto es una API sencilla de autenticación implementada con **Django** y **Django REST Framework**. Proporciona un mecanismo de inicio de sesión, registro de usuarios y obtención de tokens JWT empleando `rest_framework_simplejwt`. También incluye soporte CORS para permitir peticiones desde un cliente front‑end. Ahora incorpora un proveedor **OAuth2** mediante `django-oauth-toolkit` para facilitar la identidad federada.
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

   De forma predeterminada la aplicación usa SQLite para desarrollo. Para un
   entorno de producción establece `DEBUG=False` y configura las variables
   `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST` y
   `POSTGRES_PORT` en el archivo `.env`.
   
   También puedes definir `FRONTEND_LOGIN_URL` para que las vistas de Django
   redirijan al formulario de inicio de sesión de React cuando sea necesario.

4. Aplicar migraciones (incluyen las tablas de `django-oauth-toolkit`) y ejecutar el servidor de desarrollo:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Endpoints principales

- `POST /sso/token/cookie/` — inicio de sesión, devuelve el token de acceso y guarda el token de refresco en una cookie.
- `POST /sso/token/refresh/` — renueva el token de acceso utilizando la cookie de refresco.
- `POST /sso/logout/` — cierra la sesión eliminando la cookie de refresco.
- `GET /sso/me/` — devuelve el email y el UUID del usuario autenticado.
- `POST /sso/register/` — crea un nuevo usuario.

Para flujos OAuth2 estándar puedes utilizar los endpoints incluidos bajo la ruta `/o/` que proporciona `django-oauth-toolkit` (por ejemplo `POST /o/token/` para obtener un token de acceso).

Todos los endpoints anteriores se definen en el módulo `sso`.

## Consumo del API con JWT

El inicio de sesión se realiza enviando las credenciales al endpoint
`/api/token/cookie/`. La respuesta incluye el **access token** y almacena el
**refresh token** en una cookie denominada `refresh_token`.

```bash
curl -X POST http://localhost:8000/api/token/cookie/ \
     -H "Content-Type: application/json" \
     -d '{"email": "usuario@example.com", "password": "contraseña"}'
```

Para acceder a un recurso protegido se utiliza el token de acceso en la cabecera
`Authorization`:

```bash
curl http://localhost:8000/api/me/ \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
```

Cuando el token expira puede renovarse con la cookie de refresco:

```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
     --cookie "refresh_token=<valor>"
```

Finalmente, para cerrar la sesión basta con llamar a `/api/logout/` enviando la
misma cookie:

```bash
curl -X POST http://localhost:8000/api/logout/ \
     --cookie "refresh_token=<valor>"
```

## Consumo del API con OAuth2

`django-oauth-toolkit` expone sus endpoints bajo la ruta `/o/`. Tras crear una
aplicación OAuth2 en el panel de administración (`/admin/`), se puede obtener un
token de acceso usando el flujo `password`:

```bash
curl -X POST http://localhost:8000/o/token/ \
     -d "grant_type=password" \
     -d "username=usuario@example.com" \
     -d "password=contraseña" \
     -d "client_id=CLIENT_ID" \
     -d "client_secret=CLIENT_SECRET"
```

El token recibido se envía de la misma forma en la cabecera `Authorization`:

```bash
curl http://localhost:8000/api/me/ \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
```

## Desarrollo

El archivo `sso_backend/settings.py` configura `rest_framework_simplejwt` y `django-cors-headers`. Revisa este archivo si necesitas modificar tiempos de expiración de los tokens o el origen permitido de CORS.

## Licencia

Este proyecto se distribuye bajo los términos de la licencia MIT.
