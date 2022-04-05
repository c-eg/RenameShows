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
from enum import Enum

import dotenv
import requests


class TVDBAPI:
    """
    Class to send requests to the TV DB API.

    See: https://thetvdb.github.io/v4-api/#/ for the documentation.
    """

    def __init__(self):
        self.api_url = "https://api4.thetvdb.com/v4/"
        self.headers = {
            "Authorization": f'Bearer {os.environ.get("TV_DB")}',
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    class MediaType(Enum):
        """Class representing the media types the TVDBAPI can support."""
        MOVIE = 'movie'
        SERIES = 'series'
        PERSON = 'person'
        COMPANY = 'company'

    def search(self, query: str, media_type: MediaType = None, year: int = None) -> dict:
        """
        Searches TheMovieDatabase API for the query passed passed.

        Args:
            query: The query to search for.
            media_type: The type to restrict the search by, 'None' searches for all types.
            year: The year of the show.

        Return:
            the search response from TV DB API.
        """
        query_formatted = query.replace(" ", "%20")

        url = f"{self.api_url}search?query={query_formatted}"

        if media_type is not None:
            url += f"&type={media_type.value}"

        if year is not None:
            url += f"&year={year}"

        response = requests.get(url, headers=self.headers)

        return json.loads(response.content)


if __name__ == "__main__":
    # TODO: loading of .env should be moved to main or main's __init__ file
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TVDBAPI()
    res = temp.search(query="The Fast and The Furious", media_type=TVDBAPI.MediaType.MOVIE)
    print(res)
