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

import glob
import os

from rename_shows.api.the_movie_database_api import TheMovieDatabaseAPI
from rename_shows.util.show_info_matcher import ShowInfoMatcher


class RenameController:
    """
    Controller to rename show files.
    """

    def __init__(self):
        self.__files = []

    def load_dir(self, path: str, recursive: bool = False) -> None:
        """
        Loads a directory from the path provided.

        Args:
            path: Full path of directory.
            recursive: Whether to include subfolders or not (recursive).
        """
        new_files = glob.glob(pathname=f"{path}\\**/*.*", recursive=recursive)
        self.__files.extend(new_files)

    def rename_files(self) -> None:
        """
        Renames the files with suggestions.
        """
        for file in self.__files:
            file_name = file[file.rfind(os.sep) + 1:file.rfind('.')]

            sim = ShowInfoMatcher(file_name)
            tmdb = TheMovieDatabaseAPI()

            # tv show
            if sim.season is not None and sim.episode is not None:
                search_res = tmdb.search_tv_show(query=sim.title)

                res_0 = search_res['results'][0]
                name = res_0['name']
                _id = res_0['id']

                tmdb_episode_details = tmdb.get_tv_episode_details(_id, sim.season, sim.episode[0])

                new_title = f"{name} - S{sim.season:02}E{sim.episode[0]:02} - {tmdb_episode_details['name']}"
                print(f"{file}\n{file_name}\n{new_title}")
            # movie
            else:
                search_res = tmdb.search_movie(query=sim.title)

                res_0 = search_res['results'][0]
                title = res_0['title']
                year = res_0['release_date']

                new_title = f"{title} ({year})"

                print(f"{file}\n{file_name}\n{new_title}")
            
            print()
