# FastAPI Mike — Control de Usuarios (act4)

API REST construida con **FastAPI** y **SQLModel** para el registro, consulta, actualización y eliminación (CRUD) de usuarios. Este es el punto de entrada de la aplicación y el lugar donde se ensamblan todas las piezas del proyecto.

## Estructura del proyecto

```
act4/
├── main.py              # Punto de entrada: crea la app FastAPI y conecta todo
├── docker-compose.yml    # Levanta la base de datos PostgreSQL en un contenedor
├── mikedb.db             # Base de datos SQLite (se usa si no hay PostgreSQL configurado)
├── api/                  # Rutas / endpoints de la API
├── core/                 # Configuración transversal (seguridad, CORS)
├── db/                   # Conexión y sesión de base de datos
├── models/               # Modelos de datos (tablas SQLModel)
└── schemas/               # Esquemas Pydantic para validar entradas/salidas
```

## Función de cada carpeta

- **`api/`** — Define los endpoints HTTP (crear, listar, obtener, actualizar y eliminar usuarios).
- **`core/`** — Utilidades de configuración que usa toda la app: hashing de contraseñas (seguridad) y política CORS.
- **`db/`** — Configura el motor de base de datos y provee la sesión que usan los endpoints.
- **`models/`** — Define la tabla `User` tal como se guarda en la base de datos (SQLModel).
- **`schemas/`** — Define qué datos puede enviar/recibir el cliente (Pydantic), separado del modelo de base de datos.

## Cómo se conecta todo

1. `main.py` crea la aplicación FastAPI, configura el ciclo de vida (crea las tablas al iniciar) y registra el router de `api/user_api.py` bajo el prefijo `/api/v1/users`.
2. Cada request a `/api/v1/users` pasa por `api/user_api.py`, que usa `db/database.py` para obtener una sesión de base de datos, `schemas/user_schema.py` para validar los datos de entrada/salida, `models/user_model.py` para leer/escribir en la tabla `User`, y `core/security.py` para hashear/verificar contraseñas.
3. `core/cors.py` se aplica una sola vez en `main.py` para permitir peticiones desde otros orígenes (por ejemplo, un frontend).

## Base de datos

Por defecto usa SQLite (`mikedb.db`). Si se define la variable de entorno `DATABASE_URL` (por ejemplo apuntando al contenedor de `docker-compose.yml`), se usa PostgreSQL en su lugar.

## Cómo ejecutar

```bash
# (Opcional) levantar PostgreSQL con Docker
docker compose up -d

# Instalar dependencias e iniciar la API
pip install -r requirements.txt
uvicorn main:app --reload
```

La documentación interactiva de la API queda disponible en `/docs` una vez que el servidor está corriendo.
