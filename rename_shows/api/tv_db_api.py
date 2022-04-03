"""
This file is part of RenameShows.

RenameShows is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

RenameShows is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with RenameShows.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
import os

import dotenv
import requests


class TVDBAPI:
    """
    Class to send requests to the TV DB API.

    See: https://thetvdb.github.io/v4-api/#/ for the documentation.
    """

    BASE_URL = "https://api4.thetvdb.com/v4/"
    HEADERS = {
        "Authorization": f'Bearer {os.environ.get("TV_DB")}',
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    @staticmethod
    def search(query: str, media_type: str = None, year: int = None) -> dict:
        """
        Searches TheMovieDatabase API for the query passed passed.

        Args:
            query: The query to search for.
            media_type: The type to search for.
                Can be 'movie', 'series', 'person', or 'company'.
            year: The year of the show.

        Return:
            the search response from TV DB API.
        """
        pass


if __name__ == "__main__":
    # TODO: loading of .env should be moved to main or main's __init__ file
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TVDBAPI()
    temp.search("The Fast and The Furious")
