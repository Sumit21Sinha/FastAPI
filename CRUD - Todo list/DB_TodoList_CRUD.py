from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Integer, Text, create_engine, Column
from starlette import status

app = FastAPI()

#Creating engine and table
engine = create_engine("sqlite:///todoss.db", connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(Text)
Base.metadata.create_all(bind=engine)

#Creating session and cursor
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

#Create
@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
    todo = Todo(title=title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"message" : "Todo created successfully.", "data" : todo}

#Read
@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    todo = db.query(Todo).all()
    return todo

#Update
@app.put("/todos/{id}")
def update_todo(id : int, title : str, db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todo.title = title
    db.commit()
    db.refresh(todo)
    return todo

#Delete
@app.delete("/todos/{id}")
def delete_todo(id : int, db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message" : "Deleted successfully."}