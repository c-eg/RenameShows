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
from abc import ABC

import requests
from rename_shows.core.api.api_error import ApiError


class ShowAPI(ABC):
    """
    Class to represent a Show API.
    """

    def __init__(self):
        self.session = requests.Session()

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

        raise ApiError(response.status_code, response.reason)
