# `db/`

Todo lo relacionado con la conexión a la base de datos: motor, sesiones y creación de tablas.

## Estructura

```
db/
└── database.py   # Configuración del engine y manejo de sesiones
```

## Función

`database.py`:

- Lee la variable de entorno `DATABASE_URL` (usando `python-dotenv`). Si no existe, usa SQLite localmente (`sqlite:///./mikedb.db`) para que el proyecto funcione sin configuración extra.
- Crea el `engine` de SQLModel/SQLAlchemy que se usa en toda la app.
- `create_db_and_tables()` — crea las tablas en la base de datos a partir de los modelos (`models/`). Se llama una vez al iniciar la app, desde `main.py`.
- `get_session()` — función generadora que entrega una sesión de base de datos por request. Se inyecta como dependencia (`Depends(get_session)`) en los endpoints de `api/user_api.py`.
