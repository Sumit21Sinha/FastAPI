from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind = engine)
session = SessionLocal()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(bind = engine)

@app.post("/users")
def create_user(id : int, name : str, email : str):
    user = User(id = id, name = name, email = email)
    session.add(user)
    session.commit()

@app.get("/users")
def get_users():
    users = session.query(User).all()
    return users