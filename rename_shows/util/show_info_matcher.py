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
from typing import Union


class ShowInfoMatcher:
    """
    Class to match show information from a the file name passed.
    """
    def __str__(self):
        return  self.to_dictionary()

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.title: str = self.__match_title()
        self.year: str = self.__match_year()
        self.resolution: str = self.__match_resolution()
        self.source: str = self.__match_source()
        self.video_codec: str = self.__match_video_codec()
        self.audio: str = self.__match_audio()
        self.language: str = self.__match_language()
        self.edition: str = self.__match_edition()
        self.tags: str = self.__match_tags()
        self.release_info: str = self.__match_release_info()
        self.season: int = self.__match_season()
        self.episode: int = self.__match_episode()
        self.release_group: str = self.__match_release_group()

    def to_dictionary(self) -> dict:
        """
        Returns show info as a dictionary.
        """
        return {
            "title": self.title,
            "year": self.year,
            "resolution": self.resolution,
            "source": self.source,
            "video_codec": self.video_codec,
            "audio": self.audio,
            "language": self.language,
            "edition": self.edition,
            "tags": self.tags,
            "release_info": self.release_info,
            "season": self.season,
            "episode": self.episode,
            "release_group": self.release_group,
        }

    def __match_title(self) -> Union[str, None]:
        """
        Matches the title of the show.
        """
        regex = "(.*?)(\\W| - )(directors(.?)cut|480p|720p|1080p|dvdrip|xvid|cd[0-9]|bluray|dvdscr|brrip|divx|S[0-9]{1,3}E[0-9]{1,3}|Season[\\s,0-9]{1,4}|[\\{\\(\\[]?[0-9]{4}).*"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(1).replace(".", " ").strip()  # remove leading and trailing whitespace
        else:
            return None

    def __match_year(self) -> Union[str, None]:
        """
        Matches the year of the show.
        """
        regex = "[\\.\\s](?!^)[1,2]\\d{3}[\\.\\s]"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0).strip('.')  # remove leading and trailing '.'
        else:
            return None

    def __match_resolution(self) -> Union[str, None]:
        """
        Matches the resoltion of the show.
        """
        regex = "\\d{3,4}p"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    def __match_source(self) -> Union[str, None]:
        """
        Matches the source of the show.
        """
        regex = "[\\.\\s](CAM|(DVD|BD)SCR|SCR|DDC|R5[\\.\\s]LINE|R5|(DVD|HD|BR|BD|WEB)Rip|DVDR|(HD|PD)TV|WEB-DL|WEBDL|BluRay|Blu-Ray|TS(?!C)|TELESYNC)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    def __match_video_codec(self) -> Union[str, None]:
        """
        Matches the video codec of the show.
        """
        regex = "[\\.\\s](NTSC|PAL|[xh][\\.\\s]?264|[xh][\\.\\s]?265|H264|H265)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    def __match_audio(self) -> Union[str, None]:
        """
        Matches the audio of the show.
        """
        regex = "AAC2[\\.\\s]0|AAC|AC3|DTS|DD5[\\.\\s]1"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    def __match_language(self) -> Union[str, None]:
        """
        Matches the language of the show.
        """
        regex = "[\\.\\s](MULTiSUBS|MULTi|NORDiC|DANiSH|SWEDiSH|NORWEGiAN|GERMAN|iTALiAN|FRENCH|SPANiSH)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    def __match_edition(self) -> Union[str, None]:
        """
        Matches the edition of the show.
        """
        regex = "UNRATED|DC|(Directors|EXTENDED)[\\.\\s](CUT|EDITION)|EXTENDED|3D|2D|\\bNF\\b"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    def __match_tags(self) -> Union[str, None]:
        """
        Matches the tags of the show.
        """
        regex = "COMPLETE|LiMiTED|iNTERNAL"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)
        else:
            return None

    def __match_release_info(self) -> Union[str, None]:
        """
        Matches the release info of the show.
        """
        regex = "[\\.\\s](REAL[\\.\\s]PROPER|PROPER|REPACK|READNFO|READ[\\.\\s]NFO|DiRFiX|NFOFiX)"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None

    def __match_season(self) -> Union[int, None]:
        """
        Matches the season of the show.
        """
        regex = "(?:s|season(?:[\\.\\s]?))(\\d{1,2})"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return int(matcher.group(1))
        else:
            return None

    def __match_episode(self) -> Union[str, None]:
        """
        Function to match the episode number from the showFile passed.

        Works in formats:
        - episode/eXXX
        - episode/eXXXeXXXeXXX
        - episode/eXXX-XXX-XXX

        :return: episode number of show, or null it if doesn't exist
        """
        regex = "e(?:(\\d{1,3})|(\\d{1,3}([e-]\\d{1,3})+))"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0).replace("e|-", ",")  # not sure if this is right but it was from java so?
        else:
            return None

    def __match_release_group(self) -> Union[str, None]:
        """
        Matches the release group of the show.
        """
        regex = "- ?([^\\-. ]+)$"
        pattern = re.compile(regex, flags=re.IGNORECASE)
        matcher = pattern.search(self.__file_name)

        if matcher:
            return matcher.group(0)[1:]
        else:
            return None
