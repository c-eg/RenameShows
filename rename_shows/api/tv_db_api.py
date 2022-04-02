import json
import os

import dotenv
import requests


class TVDBAPI:
    """
    Class to send requests to the TV DB API.

    See: https://thetvdb.github.io/v4-api/#/ for the documentation.
    """

    def __init__(self):
        self.BASE_URL = "https://api4.thetvdb.com/v4/"
        self.HEADERS = {
            'Authorization': f'Bearer {os.environ.get("TV_DB")}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def search(self, query: str, type: str = None, year: int = None) -> dict:
        pass

if __name__ == "__main__":
    # TODO: loading of .env should be moved to main or main's __init__ file
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TVDBAPI()
    temp.search("The Fast and The Furious")
