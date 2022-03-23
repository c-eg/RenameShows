# RenameShows
[![License](https://img.shields.io/github/license/c-eg/RenameShows)](LICENSE) 

Renames shows passed in to the specified format.

## Planned features
### Movie Database APIs
These are the show database APIs we wish to integrate with.
- [ ] [The Movie Database (TMDB)](https://www.themoviedb.org/)
- [ ] [tvdv](https://thetvdb.com/)
- [ ] [AniDB](https://anidb.net/)

### Graphical User Interface
We plan to implement a React.js front end interface using Electron.

### Command Line Interface
We plan to implement a Command Line Interface, supporting flags to help rename show files.

## Local Development Setup
1) In the root project folder:
```
pip install -e .
```
2) Copy `.env_template` and rename the copy to `.env`
3) Go to the different API providers for movie, tv & anmie ([Movie Database APIs](#movie-database-apis)), create an account and generate an API token
    1) For The Movie Database API, you will need to generate a "API Read Access Token (v4 auth)"
4) Paste the API keys in the .env for the respective setting

## Contributors
 - Conor Egan (c-eg)
 - Christopher Sutcliffe (chris-sutcliffe)

## License
GNU General Public License v3.0
