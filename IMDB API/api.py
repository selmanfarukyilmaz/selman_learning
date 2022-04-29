"""
Requests Documentation: https://docs.python-requests.org/en/latest
IMDb API Documentation: https://imdb-api.com
"""
import json
import pprint
import requests
from urllib.parse import urljoin


api_key = "k_twpxc8hi"
api_base_url = "https://imdb-api.com"
language = "en"

# haluk bilginer
name_id = "nm0082211"
endpoint_name = f"{language}/API/Name/{api_key}/{name_id}"
url = urljoin(api_base_url, endpoint_name)

payload = {}
headers = {}
response = requests.get(url, headers=headers, data=payload)

print(response)
print(response.text)
print(response.text.encode('utf8'))
pprint.pprint(response.text.encode('utf8'))
print(response.json())
pprint.pprint(response.json())
print(response.json().keys())
print(response.json()["id"])
print(response.json()["name"])
print(response.json()["role"])
print(response.json()["image"])
print(response.json()["summary"])
print(response.json()["birthDate"])
print(response.json()["deathDate"])
print(response.json()["awards"])
print(response.json()["height"])
print(response.json()["knownFor"])
pprint.pprint(response.json()["knownFor"])
print(response.json()["castMovies"])
pprint.pprint(response.json()["castMovies"])

x = (response.json()["castMovies"])
print(type(x))

y = (response.json())
print(type(y))

z = y["castMovies"]
pprint.pprint(z)
print(type(z))
import time
for i in z:
    x = (i["id"])



api_key = "k_twpxc8hi"
api_base_url = "https://imdb-api.com"
language = "en"

# haluk bilginer
film_id = "tt1224142"
endpoint_name = f"{language}/API/Ratings/{api_key}/{film_id}"
url = urljoin(api_base_url, endpoint_name)

payload = {}
headers = {}
response = requests.get(url, headers=headers, data=payload)
response = response.json()
pprint.pprint(response.json())
print(response["imDb"])
print(type(response))
print(response.json())

def get_ids(person_id):
    api_key = "k_twpxc8hi"
    api_base_url = "https://imdb-api.com"
    language = "en"



    endpoint_name = f"{language}/API/Name/{api_key}/{person_id}"
    url = urljoin(api_base_url, endpoint_name)

    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    ids = []
    for i in response.json()["castMovies"]:
        id = (i["id"])
        ids.append(id)

    print(ids,"ids")


    ratings = {}
    for film_id in ids:
        endpoint_rating = f"{language}/API/Ratings/{api_key}/{film_id}"
        url = urljoin(api_base_url, endpoint_rating)
        response = requests.get(url, headers=headers, data=payload).json()
        ratings[film_id] = (response["imDb"])


    for rate in ratings.values():


        print(sort_orders,"sort orders")
        top = []
        counter = 0

        for i in sort_orders:
            if counter == 3:
                break
            top.append(i)
            counter += 1

        print(top,"top")






get_ids("nm0082211")

def rateings():
    api_key = "k_twpxc8hi"
    api_base_url = "https://imdb-api.com"
    language = "en"

    film_id = "tt1224142"
    endpoint_name = f"{language}/API/Ratings/{api_key}/{film_id}"
    url = urljoin(api_base_url, endpoint_name)

    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)

