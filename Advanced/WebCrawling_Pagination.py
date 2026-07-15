from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

URL = "https://www.scrapethissite.com/pages/"

@app.get("/")
def get_link(pages : int = 1, limit: int = 5):
    response = requests.get(URL)
    if response.status_code != 200:
        return {"error": "Website not reachable"}
    soup = BeautifulSoup(response.text, "html.parser")
    title = []
    for items in soup.find_all("h3", class_="page-title"):
        title.append(items.text.strip())
    start = (pages - 1) * limit
    end = start + limit
    return {
        "title": title[start:end],
    }