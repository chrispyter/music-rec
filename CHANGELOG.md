# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2025-06-08
### Added
- Initial project structure with VS Code and virtual environment setup
- `.env` file support for managing Spotify API credentials securely
- `requirements.txt` file to specify project dependencies
- Basic Spotify API integration using Spotipy and OAuth
- Test search function to query track info using Spotify API

## [0.1.1] – 2025-06-13
### Added
- MIT License file added to project root
- `README.md` with project overview and setup instructions

## [0.1.2] – 2025-06-14
### Added
- `CHANGELOG.md` to track progress
- Git repository initialization
- GitHub remote repository setup
- Initial commit with project files

## [0.1.3] - 2025-06-22
### Added
- JSON formatting for better data structure visualization
- Track ID extraction from Spotify search results
- Installed pylast library for Last.fm API integration (setup to be completed)

### Changed
- Improved code readability with json.dumps() for API responses

### Deprecated
- Spotify API integration due to recent API restrictions with Spotify audio_features endpoint

## [0.1.4] - 2025-06-26
### Added
- Direct HTTP requests using `requests` library
- Proper API parameter structure using `params` dictionary
- Test for `artist.getSimilar` method with the rapper "Future"
- JSON formatting for readable API responses

### Removed
- Spotify API dependencies from requirements.txt

### Changed
- Main.py to use Last.fm API instead of Spotify's API

### Fixed
- Environment variable handling for API key

## [0.1.5] - 2025-06-28
### Added
- getTopTags method implementation for song tag analysis

### Removed
- Comments for self-explanatory lines of code

## [0.1.6] - 2025-06-29
### Added
- Automated retrieval of tags for multiple songs
- Organization of project tasks in GitHub Projects

### Removed
- Two planned features from README.md to clarify priorities

## [0.1.7] - 2025-07-04
### Added
- Function definition (get_track_top_tags) for track.getTopTags method to use in tag.getTopTracks function

## [0.1.8] - 2025-07-15
### Added
- SQL database schema for managing song, tag, and song-tag relationship data (`schema.sql`)
- Test script (`sql_connection_test.py`) to verify integration of Python and MySQL

## [0.1.9] - 2025-07-20
### Added
- Test folder (`tests`) containing script to test SQL connection (`sql_connection_test.py`)
- Experimental file (`sandbox.py`) to organize code used to test different API calls
- Separate file for populating song-tag database in SQL (`populate_db.py`)

## [0.1.10] - 2025-07-20
### Added
- Script in `populate_db.py` to retrieve 100 songs from popular music genres