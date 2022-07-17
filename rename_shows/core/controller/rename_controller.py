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
import threading
import time
from typing import Dict, List

from rename_shows.core.api.api_error import ApiError
from rename_shows.core.api.show_api import ShowAPI
from rename_shows.core.api.the_movie_database_api import TheMovieDatabaseAPI
from rename_shows.core.model.file import File
from rename_shows.core.model.show import Show
from rename_shows.core.util.show_info_matcher import ShowInfoMatcher

TYPES_ALLOWED = ("mp4", "mkv")


class RenameController:
    """
    Controller to rename show files.
    """

    def __init__(self, show_api: ShowAPI = TheMovieDatabaseAPI()):
        self.__files: Dict[str, List[Show]] = {}
        self.__show_api = show_api

    def _load_dir(self, file, recursive: bool = False) -> File:
        depth = self._get_depth(file.path)

        if file.is_file():
            if os.path.splitext(file)[1][1:] in TYPES_ALLOWED:
                f = File(file.path, file.name, depth, os.path.splitext(file)[1])
                self.__files[f] = []
        elif file.is_dir():
            f = File(file.path, file.name, depth)
            self.__files[f] = []

            if recursive:
                for _file in os.scandir(path=file.path):
                    self._load_dir(_file, False)

    def load_source(self, path: str, recursive: bool = False) -> None:
        """
        Loads a directory from the path provided.

        Args:
            path: Full path of directory.
            recursive: Whether to include subfolders or not (recursive).
        """
        for file in os.scandir(path=path):
            self._load_dir(file, True)
        
        # sort files by depth, largest -> smallest
        # this is needed to make sure files are renamed in the correct order
        # so the full path is maintained and still correct.
        self.__files = dict(sorted(self.__files.items(), key=lambda file: file[0].depth, reverse=recursive))

    def _get_depth(self, path: str):
        return len(path.split(os.sep))

    def _create_suggestion(self, file: File):
        """Threaded function to create a suggestion given a file."""
        title = ShowInfoMatcher.match_title(file.name)
        year = ShowInfoMatcher.match_year(file.name)
        season = ShowInfoMatcher.match_season(file.name)
        episode = ShowInfoMatcher.match_episode(file.name)

        suggestions = []

        # no match found
        if not title:
            return suggestions

        new_full_path = False

        # check for file or dir, respectively
        if file.file_ext is not False:
            new_full_path = f"{file.path}{file.file_ext}"
        else:
            new_full_path = f"{file.path}"
        
        # season - likely to be dir
        if season and not episode:
            tvs = self.__show_api.find_tv_results(title)

            if len(tvs) >= 1:
                tv = tvs[0]

                suggestion = f"{tv.title} - Season {season:02}"
                suggestion = "".join(
                    i for i in suggestion if i not in r'\/:*?"<>|'
                )  # replace invalid chars on windows

                new_full_path = new_full_path.replace(file.name, suggestion)
                suggestions.append(new_full_path)
        # tv episode
        elif season and episode:
            episodes = self.__show_api.find_tv_episode_results(
                title, season, episode[0]
            )

            episode_length = len(episode)

            if len(episodes) >= 1:
                episode_res = episodes[0]
                suggestion = False

                # multi episode
                if episode_length > 1:
                    suggestion = f"{episode_res.title} - S{episode_res.season:02}E{episode[0]:02}-E{episode[episode_length - 1]:02}"
                # single episode (normal)
                else:
                    suggestion = f"{episode_res.title} - S{episode_res.season:02}E{episode_res.episode:02} - {episode_res.name}"

                suggestion = "".join(
                    i for i in suggestion if i not in r'\/:*?"<>|'
                )  # replace invalid chars on windows

                new_full_path = new_full_path.replace(file.name, suggestion)
                suggestions.append(new_full_path)
        # movie
        else:
            movies = self.__show_api.find_movie_results(title, year)

            if len(movies) >= 1:
                movie = movies[0]

                suggestion = f"{movie.title} ({movie.year[:4]})"
                suggestion = "".join(
                    i for i in suggestion if i not in r'\/:*?"<>|'
                )  # replace invalid chars on windows

                new_full_path = new_full_path.replace(file.name, suggestion)
                suggestions.append(new_full_path)

        self.__files[file] = suggestions

    def create_suggestions(self) -> None:
        """
        Creates suggestions for each directory and file.
        """
        file_threads = []

        for file in self.__files:
            thread = threading.Thread(target=self._create_suggestion, args=(file,))
            file_threads.append(thread)
            time.sleep(0.1)
            thread.start()

        # make sure threads end before proceeding
        for thread in file_threads:
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

            try:
                os.rename(f"{file.path}", suggestions[0])
            except Exception:
                continue
