
import json
import os

import dotenv
import requests

from show_database_api import ShowDatabaseAPI


class TheMovieDatabaseAPI(ShowDatabaseAPI):
    """
    Class to send requests to The Movie Database (TMDB) API.
    """

    def __init__(self):
        self.BASE_URL = "https://api.themoviedb.org/3/"
        self.HEADERS = {
            'Authorization': f'Bearer {os.environ.get("THE_MOVIE_DB")}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def test(self):
        # example of request to api
        response = requests.request(
            method="GET",
            url=f"{self.BASE_URL}search/movie?query=Spiderman&page=1&include_adult=true",
            headers=self.HEADERS
        )

        print(json.loads(response.text))

if __name__ == "__main__":
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TheMovieDatabaseAPI()
    temp.test()
