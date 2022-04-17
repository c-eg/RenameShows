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

from rename_shows.api.api_error import ApiError
from rename_shows.api.the_movie_database_api import TheMovieDatabaseAPI
from rename_shows.util.show_info_matcher import ShowInfoMatcher


class RenameController:
    """
    Controller to rename show files.
    """

    def __init__(self):
        self.__files: dict[str, tuple[str, str] | None] = {}

    def load_dir(self, path: str, recursive: bool = False) -> None:
        """
        Loads a directory from the path provided.

        Args:
            path: Full path of directory.
            recursive: Whether to include subfolders or not (recursive).
        """
        files = glob.glob(pathname=f"{path}\\**/*.*", recursive=recursive)

        for file in files:
            self.__files[file] = None

    def rename_files(self) -> None:
        """
        Renames the files from the suggestions.
        """
        for file, suggestion in self.__files.items():
            if suggestion is None:
                continue

            new_file = file.replace(suggestion[0], suggestion[1])
            print(f"{file}\n{new_file}\n")
            os.rename(file, new_file)

    def create_rename_suggestions(self) -> None:
        """
        Creates the Suggestion objects for each file.
        """
        for file in self.__files:
            file_name = file[file.rfind(os.sep) + 1:file.rfind('.')]
            suggested_name = self._get_rename_suggestion(file_name=file_name)

            if suggested_name is None:
                continue

            self.__files[file] = (file_name, suggested_name)

    def _get_rename_suggestion(self, file_name: str) -> str:
        """
        Gets the rename suggestion using a show database API.

        TODO:
        Make API calls async or threaded so can do multiple at once.

        Make this work with any show API. Might have to make the show database api
        classes more generic so they all inherit from an interface so i can pass a
        'ShowDatabaseAPI' interface in params to allow it to rename as long as the
        ShowDatabaseAPI follows the interface rules.

        Args:
            file_name: The name of the file (not path).

        Returns:
            Suggested file name.
        """
        sim = ShowInfoMatcher(file_name)
        tmdb = TheMovieDatabaseAPI()
        new_title = file_name

        # tv show
        if sim.season is not None and sim.episode is not None:
            try:
                search_res = tmdb.search_tv_show(query=sim.title)

                res_0 = search_res.get('results')[0]
                name = res_0.get('name')
                _id = res_0.get('id')

                tmdb_episode_details = tmdb.get_tv_episode_details(_id, sim.season, sim.episode[0])

                new_title = f"{name} - S{sim.season:02}E{sim.episode[0]:02} - {tmdb_episode_details['name']}"
            except ApiError:
                new_title = None
        # movie
        else:
            try:
                search_res = tmdb.search_movie(query=sim.title)

                res_0 = search_res.get('results')[0]
                title = res_0.get('title')
                year = res_0.get('release_date')

                new_title = f"{title} ({year})"
            except ApiError:
                new_title = None

        return new_title
