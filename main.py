from functions import *
import sys


def main():
    # enter movie title: (for example)
    movieTitle = "ironman"

    # get movie's rating:
    source = 'Rotten Tomatoes'
    try:
        movieRating, movieID = get_movie_ratingAndID(movieTitle, source)
    except:
        print("Movie title is NOT correct")
        sys.exit(0)

    print(f"Title: {movieTitle}")
    print(f"\tIMDB ID: {movieID}")
    print(f"\t{source}: {movieRating}")


if __name__ == "__main__":
    main()
