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

import re
from typing import Tuple, Union


class ShowInfoMatcher:
    """
    Class to match show information from a the file name passed.
    """

    @staticmethod
    def match_title(file_name) -> Union[str, None]:
        """
        Matches the title of the show.
        """
        regex = r"(.*?)(\W| - )(directors(.?)cut|480p|720p|1080p|dvdrip|xvid|cd[0-9]|bluray|dvdscr|brrip|divx|S[0-9]{1,3}E[0-9]{1,3}|Season[\s,0-9]{1,4}|[\{\(\[]?[0-9]{4}).*"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return (
                matcher.group(1).replace(".", " ").strip()
            )  # remove leading and trailing ' '
        else:
            return None

    @staticmethod
    def match_year(file_name) -> Union[str, None]:
        """
        Matches the year of the show.
        """
        regex = r"[\.\s](?!^)[1,2]\d{3}[\.\s]"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0).strip(".")  # remove leading and trailing '.'
        else:
            return None

    @staticmethod
    def match_resolution(file_name) -> Union[str, None]:
        """
        Matches the resoltion of the show.
        """
        regex = r"\d{3,4}p"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    @staticmethod
    def match_source(file_name) -> Union[str, None]:
        """
        Matches the source of the show.
        """
        regex = r"[\.\s](CAM|(DVD|BD)SCR|SCR|DDC|R5[\.\s]LINE|R5|(DVD|HD|BR|BD|WEB)Rip|DVDR|(HD|PD)TV|WEB-DL|WEBDL|BluRay|Blu-Ray|TS(?!C)|TELESYNC)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    @staticmethod
    def match_video_codec(file_name) -> Union[str, None]:
        """
        Matches the video codec of the show.
        """
        regex = r"[\.\s](NTSC|PAL|[xh][\.\s]?264|[xh][\.\s]?265|H264|H265)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    @staticmethod
    def match_audio(file_name) -> Union[str, None]:
        """
        Matches the audio of the show.
        """
        regex = r"AAC2[\.\s]0|AAC|AC3|DTS|DD5[\.\s]1"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    @staticmethod
    def match_language(file_name) -> Union[str, None]:
        """
        Matches the language of the show.
        """
        regex = r"[\.\s](MULTiSUBS|MULTi|NORDiC|DANiSH|SWEDiSH|NORWEGiAN|GERMAN|iTALiAN|FRENCH|SPANiSH)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    @staticmethod
    def match_edition(file_name) -> Union[str, None]:
        """
        Matches the edition of the show.
        """
        regex = r"UNRATED|DC|(Directors|EXTENDED)[\.\s](CUT|EDITION)|EXTENDED|3D|2D|\bNF\b"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    @staticmethod
    def match_tags(file_name) -> Union[str, None]:
        """
        Matches the tags of the show.
        """
        regex = r"COMPLETE|LiMiTED|iNTERNAL"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    @staticmethod
    def match_release_info(file_name) -> Union[str, None]:
        """
        Matches the release info of the show.
        """
        regex = r"[\.\s](REAL[\.\s]PROPER|PROPER|REPACK|READNFO|READ[\.\s]NFO|DiRFiX|NFOFiX)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    @staticmethod
    def match_season(file_name) -> Union[int, None]:
        """
        Matches the season of the show.
        """
        regex = r"s(?:eason)?\s*(\d{1,2})"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return int(matcher.group(1))
        else:
            return None

    @staticmethod
    def match_episode(file_name) -> Union[Tuple[int], None]:
        """
        Function to match the episode number from the showFile passed.

        Works in formats:
        - eXXX      | episodeXXX
        - eXXXeXXX  | episodeXXXeXXX
        - eXXX-XXX  | episodeXXX-XXX
        - eXXX-eXXX | episodeXXX-eXXX
        - eXXXYYY   | episodeXXXYYY

        :return: tuple of episode numbers or None if none
        """
        regex = (
            # r"e(?:pisode)?\s*(\d{1,3}(?!\d)|\d\d\d??)(?:-?e?(\d{1,3}))?(?!\d)"
            r"e(?:pisode\s*)?(\d{1,3}(?!\d)|\d\d\d??)(?:-?e?(\d{1,3}))?(?!\d)"
        )
        pattern = re.compile(regex, flags=re.IGNORECASE)

        result = pattern.findall(file_name)
        episodes = []

        for res in result:
            for item in res:
                if item is not None and item != "":
                    episodes.append(int(item))

        if len(episodes) > 0:
            return tuple(episodes)
        else:
            return None

    @staticmethod
    def match_release_group(file_name) -> Union[str, None]:
        """
        Matches the release group of the show.
        """
        regex = r"- ?([^\-. ]+)$"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None
