from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)

@app.get("/")
@limiter.limit("5/minute")
def home(request: Request):
    return {"message": "Welcome to FastAPI!"}