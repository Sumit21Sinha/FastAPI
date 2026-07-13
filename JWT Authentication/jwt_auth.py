from fastapi import FastAPI, Depends, HTTPException, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

from starlette import status

app = FastAPI()

SECRET_KEY = 'Sumit123'
ALGORITHM = 'HS256'

def create_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = 30)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return token

@app.post("/login")
def login(username : str, password : str):
    if username != 'Sumit' or password != 'okieokie':
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_token({"username": username})
    return {"token": token}

def verify_token(token : str = Header(None)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

@app.get("/secure")
def secure(user = Depends(verify_token)):
    return{"message: " : "User verified", "data" : user}