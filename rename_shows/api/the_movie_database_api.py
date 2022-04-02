
import json
import os

import dotenv
import requests


class TheMovieDatabaseAPI:
    """
    Class to send requests to The Movie Database (TMDB) API.

    See https://developers.themoviedb.org/3/getting-started/introduction for the documentation.
    """

    def __init__(self):
        self.BASE_URL = "https://api.themoviedb.org/3/"
        self.HEADERS = {
            'Authorization': f'Bearer {os.environ.get("THE_MOVIE_DB")}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def search_movie(self, query: str, page: int = 1, include_adult: bool = True, year: int = None) -> dict:
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
        query_formatted = query.replace(' ', "%20")

        url = f"{self.BASE_URL}search/movie?query={query_formatted}&page={page}&include_adult={include_adult}"

        if year is not None:
            url += f"&year={year}"

        response = requests.get(url, headers=self.HEADERS)

        return json.loads(response.content)

    def get_movie_details(self, movie_id: int) -> dict:
        """
        Gets the movie details from the id provided.

        Args:
            movie_id: TheMovieDatabase movie ID.

        Return:
            The details of the movie.
        """
        url = f"{self.BASE_URL}movie/{movie_id}"

        response = requests.get(url, headers=self.HEADERS)

        return json.loads(response.content)

    def search_tv_show(self, query: str, page: int = 1, include_adult: bool = True) -> dict:
        """
        Searches TheMovieDatabase API for the tv show passed.
        
        Args:
            query: The tv show to search for.
            page: What page to look on for search results.
            include_adult: Whether to include adult content in the search results.

        Return:
            The search response from TheMovieDatabase API.
        """
        query_formatted = query.replace(' ', "%20")

        url = f"{self.BASE_URL}search/tv?query={query_formatted}&page={page}&include_adult={include_adult}"

        response = requests.get(url, headers=self.HEADERS)

        return json.loads(response.content)

    def get_tv_details(self, tv_id: int) -> dict:
        """
        Gets the tv show details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.

        Return:
            The details of the tv show.
        """
        url = f"{self.BASE_URL}tv/{tv_id}"

        response = requests.get(url, headers=self.HEADERS)

        return json.loads(response.content)

    def get_tv_season_details(self, tv_id: int, season: int) -> dict:
        """
        Gets the tv show season details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.
            season: The season to get details for.

        Return:
            The season details of the tv show.
        """
        url = f"{self.BASE_URL}tv/{tv_id}/season/{season}"

        response = requests.get(url, headers=self.HEADERS)

        return json.loads(response.content)

    def get_tv_episode_details(self, tv_id: int, season: int, episode: int) -> dict:
        """
        Gets the tv show episode details from the id provided.

        Args:
            tv_id: TheMovieDatabase tv ID.
            season: The season to get details for.
            episode: The episode to get details for.

        Return:
            The episode details of the tv show.
        """
        url = f"{self.BASE_URL}tv/{tv_id}/season/{season}/epiosde/{episode}"

        response = requests.get(url, headers=self.HEADERS)

        return json.loads(response.content)

if __name__ == "__main__":
    # TODO: loading of .env should be moved to main or main's __init__ file
    dotenv.load_dotenv(dotenv.find_dotenv())  # load .env file
    temp = TheMovieDatabaseAPI()
    temp.search_movie("The Fast and The Furious")
