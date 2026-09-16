# comando para correr el programa:  uv run fastapi dev


from contextlib import asynccontextmanager
from fastapi import FastAPI

#importación de archivos previos
from db.database import create_db_and_tables
#from api.v1.user import *
#from core.cors import setup_cors

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup: se ejecuta al iniciar
    print("Iniciando BD...")
    create_db_and_tables()
    yield
    #shutdown se ejecuta al cerrar (aqui se pueden cerrar conexiones)
    print("Cerrando aplicación")

app = FastAPI(
    title="FastApi Sidrac",
    description= "primera app con Fastapi",
    version="1.0.0",
    lifespan= lifespan # aquí está el cambio clave
)

@app.get("/")
def root():
    return{"message": "Bienvenido a Fastapi Sidrac"}