from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users=[]

class User(BaseModel):
    id : int
    name : str
    age : int
    password : str

class ResponseModel(BaseModel):
    id : int
    name : str
    age : int

@app.post("/user")
def create_user(data : User):
    users.append(data)
    return {"message": "User created successfully"}

@app.get("/user/{id}", response_model = ResponseModel)
def user(id: int,  notify : bool = True):
    for user in users:
        if user.id == id:
            return user
    return {"message": "User does not exist"}