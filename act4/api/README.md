# `api/`

Contiene las rutas (endpoints) HTTP de la API, organizadas en un `APIRouter` de FastAPI.

## Estructura

```
api/
└── user_api.py   # Endpoints CRUD para el recurso "usuario"
```

## Función

`user_api.py` define el `router` que `main.py` registra bajo el prefijo `/api/v1/users`. Implementa las cinco operaciones básicas sobre usuarios:

| Método | Ruta | Función |
|---|---|---|
| `POST` | `/` | Crea un usuario nuevo (valida que email y username no existan, hashea la contraseña) |
| `GET` | `/` | Lista todos los usuarios |
| `GET` | `/{user_id}` | Obtiene un usuario por su ID |
| `PUT` | `/{user_id}` | Actualiza parcialmente un usuario existente |
| `DELETE` | `/{user_id}` | Elimina un usuario |

## Dependencias que usa

- `db.database.get_session` — para obtener una sesión de base de datos por cada request.
- `models.user_model.User` — el modelo de tabla sobre el que se hacen las consultas.
- `schemas.user_schema` (`UserCreate`, `UserUpdate`, `UserResponse`) — para validar entradas y dar forma a las respuestas.
- `core.security` (`get_password_hash`, `verify_password`) — para no guardar contraseñas en texto plano.

Cada endpoint devuelve errores HTTP explícitos (`400`, `404`) cuando corresponde, en vez de dejar que fallen silenciosamente.
