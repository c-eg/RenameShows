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

import dotenv

from rename_shows.api.the_movie_database_api import TheMovieDatabaseAPI
from rename_shows.util.show_info_matcher import ShowInfoMatcher


def main():
    """For testing."""
    test = ShowInfoMatcher("The.Fast.And.The.Furious.Tokyo.Drift.2004.1080p.blueray")
    query = test.title

    tmbd = TheMovieDatabaseAPI()
    search_res = tmbd.search_movie(query=query)

    new_title = search_res['results'][0]['title']

    print(f"{query} --> {new_title}")



if __name__ == "__main__":
    dotenv.load_dotenv(dotenv.find_dotenv())
    main()
