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

import os

import dotenv
from rename_shows.core.api.api_error import ApiError
from rename_shows.core.api.show_api import ShowAPI
from rename_shows.core.model.episode import Episode
from rename_shows.core.model.movie import Movie

dotenv.load_dotenv(dotenv.find_dotenv())

class TheMovieDatabaseAPI(ShowAPI):
    """
    Class to send requests to The Movie Database (TMDB) API.

    See https://developers.themoviedb.org/3/getting-started/introduction for the documentation.
    """

    def __init__(self):
        super().__init__()

        self.api_url = "https://api.themoviedb.org/3/"
        self.session.headers.update(
            {
                "Authorization": f'Bearer {os.getenv("THE_MOVIE_DB")}',
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def find_movie_results(self, __title: str, __year: int = None) -> list[Movie]:
        movies = []
        search_res = self._search_movie(query=__title, year=__year)
        results = search_res.get('results')

        for res in results:
            title = res.get('title', None)
            year = res.get('release_date', None)

            movie = Movie(title, year)
            movies.append(movie)

        return movies

    def find_tv_episode_results(self, __title: str, __season: int, __episode: int) -> list[Episode]:
        episodes = []
        search_res = self._search_tv_show(__title)
        results = search_res.get('results')

        for res in results:
            episode_title = res.get('name')
            _id = res.get('id')

            try:
                episode_details = self._get_tv_episode_details(_id, __season, __episode)
                episode_name = episode_details.get('name', None)

                episode = Episode(episode_title, __season, __episode, episode_name)
                episodes.append(episode)
            except ApiError:
                continue

        return episodes

    def _search_movie(
        self, __query: str, __page: int = 1, __include_adult: bool = True, __year: int = None
    ) -> dict:
        """
        Searches TheMovieDatabase API for the movie passed.

        Args:
            __query: The movie to search for.
            __page: What page to look on for search results.
            __include_adult: Whether to include adult content in the search results.
            __year: The year of the show being searched.

        Return:
            The search response from TheMovieDatabase API.

        Raises:
            ApiError: If the API request fails.
        """
        query_formatted = __query.replace(" ", "%20")

        url = (
            f"{self.api_url}search/movie?query={query_formatted}"
            f"&page={__page}&include_adult={__include_adult}"
        )

        if __year is not None:
            url += f"&year={__year}"

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def _get_movie_details(self, __movie_id: int) -> dict:
        """
        Gets the movie details from the id provided.

        Args:
            movie_id: TheMovieDatabase movie ID.

        Return:
            The details of the movie.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}movie/{__movie_id}"

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def _search_tv_show(
        self, __query: str, __page: int = 1, __include_adult: bool = True
    ) -> dict:
        """
        Searches TheMovieDatabase API for the tv show passed.

        Args:
            __query: The tv show to search for.
            __page: What page to look on for search results.
            __include_adult: Whether to include adult content in the search results.

        Return:
            The search response from TheMovieDatabase API.

        Raises:
            ApiError: If the API request fails.
        """
        query_formatted = __query.replace(" ", "%20")

        url = (
            f"{self.api_url}search/tv?query={query_formatted}"
            f"&page={__page}&include_adult={__include_adult}"
        )

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def _get_tv_details(self, __tv_id: int) -> dict:
        """
        Gets the tv show details from the id provided.

        Args:
            __tv_id: TheMovieDatabase tv ID.

        Return:
            The details of the tv show.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}tv/{__tv_id}"

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def _get_tv_season_details(self, __tv_id: int, season: int) -> dict:
        """
        Gets the tv show season details from the id provided.

        Args:
            __tv_id: TheMovieDatabase tv ID.
            __season: The season to get details for.

        Return:
            The season details of the tv show.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}tv/{__tv_id}/season/{season}"

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

    def _get_tv_episode_details(self, __tv_id: int, __season: int, __episode: int) -> dict:
        """
        Gets the tv show episode details from the id provided.

        Args:
            __tv_id: TheMovieDatabase tv ID.
            __season: The season to get details for.
            __episode: The episode to get details for.

        Return:
            The episode details of the tv show.

        Raises:
            ApiError: If the API request fails.
        """
        url = f"{self.api_url}tv/{__tv_id}/season/{__season}/episode/{__episode}"

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception
