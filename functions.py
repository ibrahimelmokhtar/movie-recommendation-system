# required packages:
import requests
import json

# enter the required api-keys:
omdb_apikey = input("Enter your OMDB api-key: ")


# returns data about specific movie using OMDB API:
def get_movie_data(movieTitle):
    """
    input   : the title of desired movie
    output  : json data about that specific movie
    """

    baseurl = f"http://www.omdbapi.com/?apikey={omdb_apikey}"

    params = {}
    params['t'] = movieTitle    # t: movie title to search for

    response = requests.get(baseurl, params=params)
    print(f"Fetching URL: {response.url}")

    return response.json()
