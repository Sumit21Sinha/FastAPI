from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/user/{id}")
def user_post(id : int, name :str):
    return {"id": id, "name": name}

class User(BaseModel):
    name : str
    age : int
@app.post("/pydantic")
def pydantic(user : User):
    return {"age": user.age, "name": user.name}