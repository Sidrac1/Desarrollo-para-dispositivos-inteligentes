# `models/`

Modelos de datos que representan las tablas reales de la base de datos, usando **SQLModel** (Pydantic + SQLAlchemy).

## Estructura

```
models/
└── user_model.py   # Modelo de tabla "User"
```

## Función

`user_model.py` define la clase `User(SQLModel, table=True)`, que representa la tabla `users` en la base de datos:

| Campo | Tipo | Notas |
|---|---|---|
| `id` | `int` (opcional) | Llave primaria autogenerada por la base de datos |
| `username` | `str` | Único, indexado, 3–50 caracteres |
| `email` | `str` | Único, indexado |
| `hashed_password` | `str` | Contraseña ya hasheada (nunca texto plano) |
| `is_active` | `bool` | `True` por defecto |
| `created_at` | `datetime` | Se asigna automáticamente al crear el registro |

Esta clase es distinta de los esquemas en `schemas/`: `User` describe cómo se guarda el dato en la base de datos, mientras que los esquemas describen qué datos puede enviar/recibir un cliente de la API.
