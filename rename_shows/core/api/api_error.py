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


class ApiError(Exception):
    """
    Exception to for any error a show api gives.

    Attributes:
        status_code: The status code from the API request.
        reason: The reason the API request failed.
    """

    def __init__(self, status_code: int, reason: str):
        self.status_code = status_code
        self.reason = reason
        message = f"API Error:\nStatus Code: {self.status_code}\nReason: {self.reason}"
        super().__init__(message)
