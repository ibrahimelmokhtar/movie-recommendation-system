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

    return response.json()


# returns movie rating and IMDB ID for specific movie title:
def get_movie_ratingAndID(movieTitle, source_name='Rotten Tomatoes'):
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

# returns data about movies similar to specific movie using TMDB API:
def get_similar_movies(movieID):
    """
    input   : movie IMDB ID
    output  : json data with movies similar to that specific movie
    """

    baseurl = f"https://api.themoviedb.org/3/movie/{movieID}/similar?api_key={tmdb_apikey}&language=en-US&page=1"
    response = requests.get(baseurl)

    return response.json()


def get_similar_movies_data(movieID):
    """
    input   : movie IMDB ID
    output  : similar movies specific data
                in form of: {'title': ['movieID', 'movieRating'], ...}
    """

    # get similar movies:
    tmdb_results = get_similar_movies(movieID)

    # collect all acquired titles:
    titles = []
    for result in tmdb_results['results']:
        titles.append(result['title'])

    # get similar movies' data:
    moviesData = {}
    for title in titles:
        try:
            (movieRating, movieID) = get_movie_ratingAndID(title)
            moviesData[title] = movieRating
        except:
            pass

    return moviesData


def sort_similar_movies(moviesData):
    """
    input   : similar movies data
    output  : sorted movies based on ratings
    """

    sortedTitles = sorted(moviesData, key=moviesData.get, reverse=True)

    sortedMovies = []
    for title in sortedTitles:
        sortedMovies.append((title, moviesData[title]))

    return sortedMovies

def display_top_movies(sortedMovies, number):
    """
    input   :   - sorted list of movies with title and rating
                - number of items to display
    output  : NONE
    """

    if len(sortedMovies) < number:
        number = len(sortedMovies)
        print(f"There is ONLY {number} movies\n")

    for i in range(number):
        movie = sortedMovies[i]
        print(f"{movie[0]} : {movie[1]}")
