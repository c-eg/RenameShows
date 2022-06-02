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

from rename_shows.core.api.api_error import ApiError
from rename_shows.core.api.show_api import ShowAPI
from rename_shows.core.api.the_movie_database_api import TheMovieDatabaseAPI
from rename_shows.core.model.show import Show
from rename_shows.core.util.show_info_matcher import ShowInfoMatcher


class RenameController:
    """
    Controller to rename show files.
    """

    def __init__(self, show_api: ShowAPI = TheMovieDatabaseAPI()):
        self.__files: dict[str, list[Show]] = {}
        self.__show_api = show_api

    def load_dir(self, path: str, recursive: bool = False) -> None:
        """
        Loads a directory from the path provided.

        Args:
            path: Full path of directory.
            recursive: Whether to include subfolders or not (recursive).
        """
        files = glob.glob(pathname=f"{path}\\**/*.*", recursive=recursive)

        for file in files:
            self.__files[file] = []

    def create_suggestions(self) -> None:
        """
        Creates suggestions for each file.
        """
        for file in self.__files:
            # get file name from full path
            file_name_start_index = file.rfind(os.sep) + 1
            file_name_end_index = file.rfind('.')
            file_name = file[file_name_start_index:file_name_end_index]

            sim = ShowInfoMatcher(file_name)

            # tv show
            if sim.season is not None and sim.episode is not None:
                episodes = self.__show_api.find_tv_episode_results(sim.title, sim.season, sim.episode[0])
                
                for episode in episodes:
                    suggestion =  f"{episode.title} - S{episode.season}E{episode.episode} - {episode.name}"
                    new_full_path = file.replace(file_name, suggestion)
                    self.__files[file].append(new_full_path)
            # movie
            else:
                movies = self.__show_api.find_movie_results(sim.title, sim.year)

                for movie in movies:
                    suggestion = f"{movie.title} ({movie.year})"
                    new_full_path = file.replace(file_name, suggestion)
                    self.__files[file].append(new_full_path)

    def output_suggestions(self) -> None:
        """
        Outputs the original file against the suggestion.
        """
        for file, suggestions in self.__files.items():
            if not suggestions:
                continue

            print(f"{file}\n{suggestions[0]}\n")

    def rename_files(self, print_output: bool = True) -> None:
        """
        Renames the files from the suggestions.
        """
        for file, suggestions in self.__files.items():
            if not suggestions:
                continue

            if print_output:
                print(f"{file}\n{suggestions[0]}\n")

            os.rename(file, suggestions[0])
