import requests
from bs4 import BeautifulSoup
from time import sleep

for page_number in range(1,4):

    url = "https://www.feedbooks.com/top?page="+str(page_number)

    response = requests.get(url, headers={"Accept": "text/html"})

    parsed_response = BeautifulSoup(response.text, "html.parser")

    titile_elements = parsed_response.find_all("a", class_="block__item-title")

    author_elements = parsed_response.find_all("a", class_="block__item-author")

    print("\nPage Number:" , page_number)

    print("\nBook Titles:", list(map(lambda x: x.text.strip(), titile_elements)))

    print("\nBook Authors:", list(map(lambda x: x.text.strip(), author_elements)))

    sleep(1)