from fastapi import FastAPI
from schema._init_ import Item
from schema.users_schema import User
from schema.products_schema import Product
app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



@app.get("/users/{user_id}")
def get_users(user_id: int , q: str | None=None):
    return {"user_id":user_id, "q":q}

@app.put("/users/{user_id}")
def update_user(user_id:int, user : User):
    return {"message":"usuario actualizado", 
            "user_id":user_id, 
            "user_info": user
            }


@app.get("/products/{product_id}")
def read_products(product_id:int):
    return{"product_id": product_id}

@app.put("/products/{product_id}")
def update_product (product_id: int, product:Product | None=None ):
    return{"item_id":product_id, 
           "description": product}