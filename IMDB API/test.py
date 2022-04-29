import json
import pprint
import requests
from urllib.parse import urljoin

aksamavisi = "k_twpxc8hi"
selman123 = "k_nv7mp1fp"
g170904008 = "k_6eju6zra"
deneme1 = "k_ocvapa1g"
selman1 = "k_0iao0a09"


def get_top3(person_id: str):
    """
    Shows the name and IMDB rating of the 3 movies with the highest IMDB rating of the actor whose ID is entered

    :param person_id: Actor's ID in the url part of her IMDB profile.
    """
    api_key = "k_0iao0a09"
    api_base_url = "https://imdb-api.com"
    language = "en"

    endpoint_name = f"{language}/API/Name/{api_key}/{person_id}"
    url = urljoin(api_base_url, endpoint_name)
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    ids = []
    for movies in response.json()["castMovies"]:
        id = (movies["id"])
        ids.append(id)

    # pprint.pprint(ids)

    ratings = {}
    for film_id in ids:
        endpoint_rating = f"{language}/API/Ratings/{api_key}/{film_id}"
        url = urljoin(api_base_url, endpoint_rating)
        response = requests.get(url, headers=headers, data=payload).json()
        ratings[response["fullTitle"]] = (response["imDb"])

    sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)

    # print(sorted_ratings)
    print(sorted_ratings[:3])


get_top3("nm9613650")