import requests
from bs4 import BeautifulSoup

def get_india_headlines():
    url = "https://www.hindustantimes.com/india-news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for item in soup.select("h3"):
        text = item.get_text(strip=True)
        if text and len(text.split()) > 3:
            headlines.append(text)

    return headlines
