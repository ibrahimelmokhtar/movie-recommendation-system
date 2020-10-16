from functions import *
import sys


def main():
    # enter movie title: (for example)
    movieTitle = input("Enter movie title: ")

    # get movie's rating:
    source = 'Rotten Tomatoes'
    try:
        print("Processing your request ...")
        movieRating, movieID = get_movie_ratingAndID(movieTitle)
    except:
        print("Movie title is NOT correct")
        sys.exit(0)

    # get similar movies' data:
    moviesData = get_similar_movies_data(movieID)

    # sort similar movies from highest ratings to lowest ratings:
    sortedMovies = sort_similar_movies(moviesData)
    print(json.dumps(sortedMovies, indent=4))


if __name__ == "__main__":
    main()
