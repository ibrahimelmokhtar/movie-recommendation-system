from functions import *
import sys


def main():
    # enter movie title: (for example)
    movieTitle = "iron man"

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

    # get movie recommendations:
    tmdb_results = get_similar_movies(movieID)

    # collect all acquired titles:
    titles = []
    for result in tmdb_results['results']:
        titles.append(result['title'])

    # display collected titles:
    print(titles)


if __name__ == "__main__":
    main()
