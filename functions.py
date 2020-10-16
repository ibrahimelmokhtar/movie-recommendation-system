# required packages:
import requests
import json
from config import *


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


# returns movie rating and IMDB ID for specific movie title:
def get_movie_ratingAndID(movieTitle, source_name):
    """
    input   :   - the title of desired movie
            and - desired rating's source name (examples: 'Rotten Tomatoes', 'Internet Movie Database', ... etc.)
    output  : rating value and IMDB ID, both corresponding to specific source_name
    """

    # get movie json data using OMDB API:
    omdb_result = get_movie_data(movieTitle)

    # loop over all ratings to find the desired source_name:
    for rating in omdb_result['Ratings']:
        if rating['Source'] == source_name:
            (movieRating, movieID) = (rating['Value'], omdb_result['imdbID'])
            break

    return (movieRating, movieID)
