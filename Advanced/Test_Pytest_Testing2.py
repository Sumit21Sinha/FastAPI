from fastapi import FastAPI
from fastapi.testclient import TestClient
from Pytest_Testing import app

client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_post():
    response = client.post("/user/5", params={"name": "John"})
    assert response.status_code == 200
    assert response.json() == {"id": 5, "name": "John"}

def test_pydantic():
    response = client.post("/pydantic", json={"name": "John", "age": 25})
    assert response.status_code == 200
    assert response.json() == {"name": "John", "age": 25}