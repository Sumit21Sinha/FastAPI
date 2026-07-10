from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def Home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "ABOUT ME"}

@app.get("/users/{id}")
def users(id : int):
    return {"id" : id}

@app.get("/products")
def products(name : str=None, price : int=1000):
    return {"name:" : name, "price:" : price}

@app.post("/create-user")
def create_user(name : str, salary : int):
    return {"name" : name, "salary" : salary}

class product(BaseModel):
    name: str
    price: int
@app.post("/create-product")
def create_product(prod : product):
    return {"data" : prod}

class Address(BaseModel):
    street: str
    city: str
    state: str
class User2(BaseModel):
    name: str
    salary: int
    address: Address
@app.post("/create-user2")
def create_user2(data: User2):
    return {"Message:" : "User Created", "data:" : data}