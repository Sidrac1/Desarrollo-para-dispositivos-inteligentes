# `schemas/`

Esquemas de validación (Pydantic) que definen la forma de los datos que entran y salen de la API. Son independientes del modelo de base de datos (`models/`).

## Estructura

```
schemas/
└── user_schema.py   # Esquemas de entrada/salida para el recurso "usuario"
```

## Función

`user_schema.py` define tres esquemas usados por `api/user_api.py`:

- **`UserCreate`** — datos obligatorios para registrar un usuario nuevo: `username`, `email`, `password` (mínimo 8 caracteres). Se usa en `POST /`.
- **`UserUpdate`** — todos los campos son opcionales, para permitir actualizaciones parciales (el cliente solo envía lo que quiere cambiar). Se usa en `PUT /{user_id}`.
- **`UserResponse`** — lo que la API devuelve al cliente: `id`, `username`, `email`, `is_active`, `created_at`. Nunca incluye la contraseña. Usa `from_attributes = True` para poder construirse directamente a partir de un objeto `User` de `models/`.

Esta separación evita que la contraseña hasheada u otros campos internos se filtren accidentalmente en las respuestas de la API.
