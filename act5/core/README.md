# `core/`

Configuración transversal de la aplicación: piezas que no pertenecen a un endpoint en particular, pero que la app necesita para funcionar de forma segura y accesible.

## Estructura

```
core/
├── security.py   # Hashing y verificación de contraseñas
└── cors.py       # Configuración de CORS
```

## Función de cada archivo

- **`security.py`** — Configura el algoritmo **Argon2** para hashear contraseñas (`get_password_hash`) y verificarlas al hacer login (`verify_password`). Lo usa `api/user_api.py` al crear usuarios, para nunca guardar la contraseña en texto plano.
- **`cors.py`** — Define `setup_cors(app)`, que agrega el middleware `CORSMiddleware` de FastAPI a la aplicación. Por defecto permite peticiones desde cualquier origen (`["*"]`), pensado para desarrollo. `main.py` la llama una sola vez al construir la app.
