from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class User(SQLModel,table=True):
    """
    Modelo de usaurio para la base de datos
    Hereda de SQLModel (que combina Pydantix + SQLAlchemy)
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, min_length=3, max_length=50)
    email: str = Field(index=True, unique=True)
    hashed_password: str = Field(min_length= 8)
    is_active: bool = Field(default=True)
    created_at : datetime = Field(default_factory= datetime.utcnow)

    class Config:
        #Configuración opcional para la tabla
        table_name = "users"