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

import concurrent.futures
import multiprocessing
import os
import threading
from typing import List

from rename_shows.core.api.api_error import ApiError
from rename_shows.core.api.show_api import ShowAPI
from rename_shows.core.api.the_movie_database_api import TheMovieDatabaseAPI
from rename_shows.core.model.file import File
from rename_shows.core.model.show import Show
from rename_shows.core.util.show_info_matcher import ShowInfoMatcher


class RenameController:
    """
    Controller to rename show files.
    """

    def __init__(self, show_api: ShowAPI = TheMovieDatabaseAPI()):
        self.__files: dict[str, List[Show]] = {}
        self.__show_api = show_api

    def load_dir(self, path: str, recursive: bool = False) -> None:
        """
        Loads a directory from the path provided.

        Args:
            path: Full path of directory.
            recursive: Whether to include subfolders or not (recursive).
        """
        TYPES_ALLOWED = ("mp4", "mkv")

        for file in os.scandir(path=path):
            f = File(file.path, file.name)

            if file.is_dir():
                self.__files[f] = []

                if recursive:
                    self.load_dir(file.path, recursive)
            elif file.is_file():
                if os.path.splitext(file)[1][1:] in TYPES_ALLOWED:
                    self.__files[f] = []

    def _create_suggestion(self, file: File):
        """Threaded function to create a suggestion given a file."""
        sim = ShowInfoMatcher(file.name)
        suggestions = []

        # no match found
        if not sim.title:
            return suggestions

        # season
        if sim.season and not sim.episode:
            tvs = self.__show_api.find_tv_results(sim.title)

            for tv in tvs:
                suggestion = f"{tv.title}"
                suggestion = "".join(
                    i for i in suggestion if i not in r'\/:*?"<>|'
                )  # replace invalid chars on windows

                new_full_path = file.path.replace(file.name, suggestion)
                suggestions.append(new_full_path)
        # tv episode
        elif sim.season and sim.episode:
            episodes = self.__show_api.find_tv_episode_results(
                sim.title, sim.season, sim.episode[0]
            )

            for episode in episodes:
                suggestion = f"{episode.title} - S{episode.season:02}E{episode.episode:02} - {episode.name}"
                suggestion = "".join(
                    i for i in suggestion if i not in r'\/:*?"<>|'
                )  # replace invalid chars on windows

                new_full_path = file.path.replace(file.name, suggestion)
                suggestions.append(new_full_path)
        # movie
        else:
            movies = self.__show_api.find_movie_results(sim.title, sim.year)

            for movie in movies:
                suggestion = f"{movie.title} ({movie.year[:4]})"
                suggestion = "".join(
                    i for i in suggestion if i not in r'\/:*?"<>|'
                )  # replace invalid chars on windows

                new_full_path = file.path.replace(file.name, suggestion)
                suggestions.append(new_full_path)

        self.__files[file] = suggestions

    def create_suggestions(self) -> None:
        """
        Creates suggestions for each file.
        """
        threads = []

        for file in self.__files:
            thread = threading.Thread(target=self._create_suggestion, args=(file,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def output_suggestions(self) -> None:
        """
        Outputs the original file against the suggestion.
        """
        for file, suggestions in self.__files.items():
            if not suggestions:
                continue

            print(f"{file.path}\n{suggestions[0]}\n")

    def rename_files(self) -> None:
        """
        Renames the files from the suggestions.
        """
        for file, suggestions in self.__files.items():
            if not suggestions:
                continue

            os.rename(file, suggestions[0])
