from fastapi import FastAPI, HTTPException, UploadFile, File
import os
import shutil
from fastapi.staticfiles import StaticFiles

from starlette.staticfiles import StaticFiles

app = FastAPI()

upload_dir = "uploads"
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

app.mount("/files", StaticFiles(directory=upload_dir), name="files")

@app.post("/upload")
def upload(file : UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(upload_dir, filename)
    if file.filename == "":
        raise HTTPException(status_code=400, detail="No file part")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": filename, "url" : "/files/" + filename}

@app.get("/files/{filename}")
def get_file(filename : str):
    path = os.path.join(upload_dir, filename)
    return {"filename": filename, "url" : "/files/" + filename}