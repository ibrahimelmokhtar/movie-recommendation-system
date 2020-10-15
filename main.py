from functions import *


def main():
    # enter movie title: (for example)
    movieTitle = "inception"

    # get movie's rating:
    source = 'Rotten Tomatoes'
    movieRating, movieID = get_movie_ratingAndID(movieTitle, source)

    print(f"Title: {movieTitle}")
    print(f"\tIMDB ID: {movieID}")
    print(f"\t{source}: {movieRating}")


if __name__ == "__main__":
    main()
