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
from abc import ABC, abstractmethod
from typing import List

import requests
from rename_shows.core.api.api_error import ApiError
from rename_shows.core.model.episode import Episode
from rename_shows.core.model.movie import Movie
from rename_shows.core.model.tv import Tv


class ShowAPI(ABC):
    """
    Class to represent a Show API.
    """

    def __init__(self):
        self.session = requests.Session()

    @abstractmethod
    def find_movie_results(self, __title: str, __year: int) -> List[Movie]:
        """
        Find a movie from the API.

        Args:
            __title: The title of the movie.
            __year: The year of the movie.

        Returns:
            A list of movie objects containing the movie information from the API.
        """

    @abstractmethod
    def find_tv_results(self, __title: str) -> List[Tv]:
        """
        Find a tv show from the API.

        Args:
            __title: The title of the tv episode.

        Returns:
            A list of tv show objects containing the tv show information from the API.
        """

    @abstractmethod
    def find_tv_episode_results(
        self, __title: str, __season: int, __episode: int
    ) -> List[Episode]:
        """
        Find a tv episode from the API.

        Args:
            __title: The title of the tv episode.
            __season: The season of the tv episode.
            __episode: The episode of the tv episode.

        Returns:
            A list of tv episode objects containing the tv episode information from the API.
        """

    def _make_request(self, __url):
        """
        Function to make an API request.

        Args:
            __url: The url for the request.

        Raises:
            ApiError: If the API request fails.
        """
        try:
            response: requests.Response = self.session.get(__url)

            if response.status_code == 200:
                return json.loads(response.content)
            else:
                raise ApiError(response.status_code, response.reason)
        except requests.exceptions.ContentDecodingError as exception:
            raise ApiError(-3, exception.response)
