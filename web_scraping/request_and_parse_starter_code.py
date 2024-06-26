import requests
from bs4 import BeautifulSoup

url = "https://www.feedbooks.com/search?query=cat"

response = requests.get(url, headers={"Accept": "text/html"})

parsed_response = BeautifulSoup(response.text, "html.parser")

titles = parsed_response.find_all("a", class_="block__item-title")

for title in titles:
    print(title.text)