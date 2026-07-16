from bs4 import BeautifulSoup
from fastapi import FastAPI
import requests
import time

app = FastAPI()

cache = []
fetch_data = 0

@app.get("/")
def get_news():
    global cache, fetch_data
    URL = "https://www.scrapethissite.com/pages/"
    T = time.time()
    if T-fetch_data >= 60:
        print("fetching data from API")
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        cache = [items.text.strip() for items in soup.find_all("h3", class_="page-title")]
        fetch_data = time.time()
    else:
        print("Using Cache")
    return{"data":cache}

