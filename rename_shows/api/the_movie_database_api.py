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


class TheMovieDatabaseAPI:
    """
    Class to send requests to The Movie Database (TMDB) API.

    See https://developers.themoviedb.org/3/getting-started/introduction for the documentation.
    """

    BASE_URL = "https://api.themoviedb.org/3/"
    HEADERS = {
        "Authorization": f'Bearer {os.environ.get("THE_MOVIE_DB")}',
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    @staticmethod
    def search_movie(
        query: str, page: int = 1, include_adult: bool = True, year: int = None
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
        """
        query_formatted = query.replace(" ", "%20")

        url = f"{TheMovieDatabaseAPI.BASE_URL}search/movie? \
            query={query_formatted}&page={page}&include_adult={include_adult}"

        if year is not None:
            url += f"&year={year}"

        response = requests.get(url, headers=TheMovieDatabaseAPI.HEADERS)

        return json.loads(response.content)

    @staticmethod
    def get_movie_details(movie_id: int) -> dict:
        """
        Gets the movie details from the id provided.

        Args:
            movie_id: TheMovieDatabase movie ID.

        Return:
            The details of the movie.
        """
        url = f"{TheMovieDatabaseAPI.BASE_URL}movie/{movie_id}"

        response = requests.get(url, headers=TheMovieDatabaseAPI.HEADERS)

        return json.loads(response.content)

    @staticmethod
    def search_tv_show(query: str, page: int = 1, include_adult: bool = True) -> dict:
        """
        Searches TheMovieDatabase API for the tv show passed.

        Args:
            query: The tv show to search for.
            page: What page to look on for search results.
            include_adult: Whether to include adult content in the search results.

        Return:
            The search response from TheMovieDatabase API.
        """
        query_formatted = query.replace(" ", "%20")

        url = f"{TheMovieDatabaseAPI.BASE_URL}search/tv? \
            query={query_formatted}&page={page}&include_adult={include_adult}"

        response = requests.get(url, headers=TheMovieDatabaseAPI.HEADERS)

        return json.loads(response.content)

    @staticmethod
    def get_tv_details(tv_id: int) -> dict:
        """
        Gets the tv show details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.

        Return:
            The details of the tv show.
        """
        url = f"{TheMovieDatabaseAPI.BASE_URL}tv/{tv_id}"

        response = requests.get(url, headers=TheMovieDatabaseAPI.HEADERS)

        return json.loads(response.content)

    @staticmethod
    def get_tv_season_details(tv_id: int, season: int) -> dict:
        """
        Gets the tv show season details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.
            season: The season to get details for.

        Return:
            The season details of the tv show.
        """
        url = f"{TheMovieDatabaseAPI.BASE_URL}tv/{tv_id}/season/{season}"

        response = requests.get(url, headers=TheMovieDatabaseAPI.HEADERS)

        return json.loads(response.content)

    @staticmethod
    def get_tv_episode_details(tv_id: int, season: int, episode: int) -> dict:
        """
        Gets the tv show episode details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.
            season: The season to get details for.
            episode: The episode to get details for.

        Return:
            The episode details of the tv show.
        """
        url = f"{TheMovieDatabaseAPI.BASE_URL}tv/{tv_id}/season/{season}/epiosde/{episode}"

        response = requests.get(url, headers=TheMovieDatabaseAPI.HEADERS)

        return json.loads(response.content)


if __name__ == "__main__":
    # TODO: loading of .env should be moved to main or main's __init__ file
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TheMovieDatabaseAPI()
    temp.search_movie("The Fast and The Furious")
