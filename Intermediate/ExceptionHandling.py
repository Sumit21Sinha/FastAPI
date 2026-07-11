from fastapi import FastAPI, status, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code = 404,
#             detail = "User Not Found"
#         )
#     return {
#         "id": 1,
#         "name":"Sumit"
#     }

class customException(Exception):
    def __init__(self, id : int):
        self.id = id
@app.exception_handler(customException)
def customhandling(request: Request, exception: customException):
    return JSONResponse(
        status_code = 404,
        content = {
            "message": f"User {exception.id } not found"
        }
    )
@app.get("/users/{user_id}")
def user(user_id: int):
    if user_id != 1:
        raise customException(user_id)
    return {"user_id": user_id}
