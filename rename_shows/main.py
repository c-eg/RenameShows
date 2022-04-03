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

from rename_shows.util.show_info_matcher import ShowInfoMatcher


def main():
    """For testing."""
    test = ShowInfoMatcher("The.Good.Place.S04E11.1080p.NF.WEB-DL.DDP5.1.x264-AJP69")
    print(test.to_dictionary())

    print("\n")

    test = ShowInfoMatcher(
        "First.Man.2018.1080p.BluRay.REMUX.AVC.Atmos-EPSiLON.torrent"
    )
    print(test.to_dictionary())

    print("\n")


if __name__ == "__main__":
    main()
