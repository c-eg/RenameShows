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
from enum import Enum

from rename_shows.core.api.api_error import ApiError
from rename_shows.core.api.show_api import ShowAPI


class TVDBAPI(ShowAPI):
    """
    Class to send requests to the TV DB API.

    See: https://thetvdb.github.io/v4-api/#/ for the documentation.
    """

    def __init__(self):
        super().__init__()

        self.api_url = "https://api4.thetvdb.com/v4/"
        self.session.headers.update(
            {
                "Authorization": f'Bearer {os.getenv("TV_DB")}',
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    class MediaType(Enum):
        """Class representing the media types the TVDBAPI can support."""

        MOVIE = "movie"
        SERIES = "series"
        PERSON = "person"
        COMPANY = "company"

    def search(
        self, __query: str, __media_type: MediaType = None, __year: int = None
    ) -> dict:
        """
        Searches TheMovieDatabase API for the query passed passed.

        Args:
            __query: The query to search for.
            __media_type: The type to restrict the search by, 'None' searches for all types.
            __year: The year of the show.

        Return:
            the search response from TV DB API.

        Raises:
            ApiError: If the API request fails.
        """
        query_formatted = __query.replace(" ", "%20")

        url = f"{self.api_url}search?query={query_formatted}"

        if __media_type is not None:
            url += f"&type={__media_type.value}"

        if __year is not None:
            url += f"&year={__year}"

        try:
            return super()._make_request(url)
        except ApiError as exception:
            raise ApiError(exception.status_code, exception.reason) from exception

