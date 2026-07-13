from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from starlette import status

app = FastAPI()

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

OAuthkey = OAuth2PasswordBearer(tokenUrl="login")
hashpass = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return hashpass.hash(password)
def verify_password(plain_password, hashed_password):
    return hashpass.verify(plain_password, hashed_password)

fake_db={"admin" : {"username": "admin", "hashed_password": hashpass.hash("1234")}}

def create_token(dicti : dict):
    encode_copy = dicti.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    encode_copy["exp"] = expire
    token = jwt.encode(encode_copy, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post("/login")
def login_user(formuser : OAuth2PasswordRequestForm = Depends()):
    if (formuser.username == fake_db["admin"]["username"] and verify_password(formuser.password, fake_db["admin"]["hashed_password"])):
        token = create_token({"username" : formuser.username})
        return {"token" : token}

def verify_token(token : str = Depends(OAuthkey)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("username")
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return username

@app.get("/secure")
def secure(data : str = Depends(verify_token)):
    return{"data":data, "message":"User Verified Succesfully"}