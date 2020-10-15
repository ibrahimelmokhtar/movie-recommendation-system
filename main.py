from functions import *


def main():
    # enter movie title: (for example)
    movieTitle = "inception"

    # get movie's data using OMDB API:
    movieData = get_movie_data(movieTitle)

    # display readable data:
    readable = json.dumps(movieData, indent=4)
    print(f"Fetched data:\n{readable}")


if __name__ == "__main__":
    main()
