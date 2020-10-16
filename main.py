from functions import *
import sys


def main():
    # enter movie title: (for example)
    movieTitle = "iron man"

    # get movie's rating:
    source = 'Rotten Tomatoes'
    try:
        movieRating, movieID = get_movie_ratingAndID(movieTitle)
    except:
        print("Movie title is NOT correct")
        sys.exit(0)

    print(f"Title: {movieTitle}")
    print(f"\tIMDB ID: {movieID}")
    print(f"\t{source}: {movieRating}")

    # get similar movies' data:
    moviesData = get_similar_movies_data(movieID)
    print(json.dumps(moviesData, indent=4))


if __name__ == "__main__":
    main()
