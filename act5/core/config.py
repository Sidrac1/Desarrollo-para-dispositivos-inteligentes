from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #configuracion de la bd
    DATABASE_URL: str

    #configuración de autenticación de JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    #Configuración de pydantyc v2
    model_config = {
        "env_file": ".env",
        "extra": "ignore" #ignora variables no declaradas en la clase
    }
settings = Settings()