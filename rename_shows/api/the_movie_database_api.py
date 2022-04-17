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
from rename_shows.api.api_error import ApiError


class TheMovieDatabaseAPI:
    """
    Class to send requests to The Movie Database (TMDB) API.

    See https://developers.themoviedb.org/3/getting-started/introduction for the documentation.
    """

    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f'Bearer {os.environ.get("THE_MOVIE_DB")}',
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def search_movie(
        self, query: str, page: int = 1, include_adult: bool = True, year: int = None
    ) -> dict:
        """
        Searches TheMovieDatabase API for the movie passed.

        Args:
            query: The movie to search for.
            page: What page to look on for search results.
            include_adult: Whether to include adult content in the search results.
            year: The year of the show being searched.

        Return:
            The search response from TheMovieDatabase API.

        Raises:
            ApiError: If the API request fails.
        """
        query_formatted = query.replace(" ", "%20")

        url = (
            f"{self.api_url}search/movie?query={query_formatted}"
            f"&page={page}&include_adult={include_adult}"
        )

        if year is not None:
            url += f"&year={year}"

        try:
            return self._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def get_movie_details(self, movie_id: int) -> dict:
        """
        Gets the movie details from the id provided.

        Args:
            movie_id: TheMovieDatabase movie ID.

        Return:
            The details of the movie.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}movie/{movie_id}"

        try:
            return self._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def search_tv_show(
        self, query: str, page: int = 1, include_adult: bool = True
    ) -> dict:
        """
        Searches TheMovieDatabase API for the tv show passed.

        Args:
            query: The tv show to search for.
            page: What page to look on for search results.
            include_adult: Whether to include adult content in the search results.

        Return:
            The search response from TheMovieDatabase API.

        Raises:
            ApiError: If the API request fails.
        """
        query_formatted = query.replace(" ", "%20")

        url = (
            f"{self.api_url}search/tv?query={query_formatted}"
            f"&page={page}&include_adult={include_adult}"
        )

        try:
            return self._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def get_tv_details(self, tv_id: int) -> dict:
        """
        Gets the tv show details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.

        Return:
            The details of the tv show.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}tv/{tv_id}"

        try:
            return self._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def get_tv_season_details(self, tv_id: int, season: int) -> dict:
        """
        Gets the tv show season details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.
            season: The season to get details for.

        Return:
            The season details of the tv show.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}tv/{tv_id}/season/{season}"

        try:
            return self._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def get_tv_episode_details(self, tv_id: int, season: int, episode: int) -> dict:
        """
        Gets the tv show episode details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.
            season: The season to get details for.
            episode: The episode to get details for.

        Return:
            The episode details of the tv show.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}tv/{tv_id}/season/{season}/episode/{episode}"

        try:
            return self._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def _make_request(self, url):
        """
        Function to make an API request for TheMovieDatabaseAPI.

        Args:
            url: The url for the request.

        Raises:
            ApiError: If the API request fails.
        """
        response: requests.Response = self.session.get(url)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise ApiError(response.status_code, response.reason)


if __name__ == "__main__":
    # TODO: loading of .env should be moved to main or main's __init__ file
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TheMovieDatabaseAPI()
    temp.search_movie("The Fast and The Furious")
