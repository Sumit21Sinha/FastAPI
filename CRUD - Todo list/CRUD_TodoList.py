from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[]

class todo(BaseModel):
    id : int
    title : str
    completed : bool
@app.post("/todo")
def create_todo(data : todo):
    todos.append(data)
    return {"message: " : "Todo Added Successfully"}

@app.get("/todo")
def get_todos():
    return todos

@app.get("/todo/{id}")
def get_todo(id : int):
    for todo in todos:
        if todo.id == id:
            return todo
    return {"Error"}

@app.put("/update-todo")
def update_todo(id : int, updata : todo):
    for index, todo in enumerate(todos):
            if todo.id == id:
                todos[index] = updata
                return{"Message" : "Updation Completed Successfully"}
    return {"Error"}

@app.delete("/del-todo/{id}")
def del_todo(id : int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(index)
            return{"Message" : "Deleted Successfully"}
    return {"Error"}