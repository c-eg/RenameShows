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
from datetime import datetime

from dotenv import find_dotenv, load_dotenv

from rename_shows.core.controller.rename_controller import RenameController


def main():
    """For testing."""
    directory = input("Directory: ")
    recursive = input("Include Subfolders?: ")
    start = datetime.now()

    rename_controller = RenameController()
    # rename_controller.load_source(path="E:\\Downloads\\Downloaded\\Errors", recursive=True)
    rename_controller.load_source(directory, recursive)
    rename_controller.create_suggestions()
    rename_controller.output_suggestions()

    rename = input("Rename? ")

    if rename == True:
        rename_controller.rename_files()

    end = datetime.now()
    print(f"Time Taken: {(end - start)}")

    input("Press enter to exit.")


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    main()
