from fastapi import FastAPI,Depends, Header, HTTPException, Request
import time

app = FastAPI()

#Middleware
@app.middleware("http")
async def middlewaretest(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    print("Time taken =", end_time - start_time)
    return response

def verify_token(token : str = Header(None)):
    if token != "Pass123":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return "Token successfully verified."
@app.get("/token")
def my_token(data = Depends(verify_token)):
    return data

def verify_tokens(token : str):
    if token != "Pass123":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return "Token successfully verified."
@app.get("/tokens")
def my_token(data = Depends(verify_tokens)):
    return { "token": data , "message" : "okie"}