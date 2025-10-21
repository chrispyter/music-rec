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

## [0.1.11] - 2025-09-03
### Added
- Error handling for edge cases when a user inputs a song that is mispelled, not real, or unknown

## [0.1.12] - 2025-09-13
### Added
- Logic to retrieve and process song name, artist name, and tags for each song using Last.fm API

### Changed
- Improved database population script to ensure only valid songs with tags are processed

## [0.1.13] - 2025-09-16
### Changed
- Retrieval of tags so only 10 tags are captured from each song
- Standardization of tag names to lowercase to ensure there aren't duplicate tags

## [0.1.14] - 2025-09-17
### Fixed
- Loop control logic in populate_db.py to properly process exactly 100 songs per genre
- Infinite loop issue caused by while loop structure repeating identical API requests

## [0.1.15] - 2025-09-18
### Fixed
- KeyError for missing 'toptags' in API responses by adding proper error handling with .get() method
- Script now successfully processes all 15 genres without crashing

### Added
- Analysis script in sandbox.py to count songs per genre from test output

## [0.1.16] - 2025-09-23
### Changed
- SQL schema to match syntax for SQLite

### Added
- More genre variations to popular_genres list to widen the variety of songs 

## [0.1.17] - 2025-09-24
### Added
- SQLite database file (music_rec_schema) with normalized table structure
- Complete SQL integration in populate_db.py with parameterized queries
- Database population script that successfully inserted 910 songs with 1,718 unique tags and 9,075 song-tag relationships
- UNIQUE constraints to prevent duplicate songs and tags

### Changed
- Database population from print statements to actual SQL INSERT operations with proper error handling

## [0.1.18] - 2025-09-30
### Added
- SQLite database connection in main.py for recommendation algorithm
- Query to check if user input song exists in database and retrieve song_id
- Error handling for songs not found in database with fallback message

## [0.1.19] - 2025-10-6
### Added
- SQL JOIN query to retrieve all tags associated with user's input song

## [0.1.20] - 2025-10-20
### Added
- SQL query to output top 5 songs that share the most tags with input song