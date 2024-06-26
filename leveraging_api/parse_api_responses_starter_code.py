import requests
import json

print("\nPRODUCT EXAMPLE 1\n")

base_url= "https://api.upcitemdb.com/prod/trial/lookup"

parameters = {"upc":"028400516686"}

response = requests.get(base_url, params=parameters)

print(response.url)

info = json.loads(response.text)

item = info["items"][0]

title = item["title"]

brand = item["brand"]

print("title:", title)

print("brand:", brand)