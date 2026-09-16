from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


#============================
#Esquemas para crear usuario
#============================
class UserCreate(BaseModel):
    """Datos necesarios para crear un usuario"""
    username: str = Field(..., min_length=3, max_length=50,description="Nombre de usuario")
    email: EmailStr = Field(...,description="Correo electrónico")
    password: str = Field(..., min_length=8, max_length=72, description="Contraseña (Mínimo 8 caracteres)")

class UserUpdate(BaseModel):
    """datos opcionales para actualizar un usuario"""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(None, min_length=8, max_length=72)
    is_active: Optional[bool] = None

class UserReponse(BaseModel):
    """Datos del usuario que se devuelven en la respuesta"""
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime

    class Config: 
        from_attributes = True

