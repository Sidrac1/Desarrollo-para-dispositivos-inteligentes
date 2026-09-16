from pydantic import BaseModel

class Product(BaseModel):
    price: float
    description:str
