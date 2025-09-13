import os
from dotenv import load_dotenv
import json
import requests
import sqlite3

load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

#  CURRENTLY FIGURING OUT HOW TO CHECK SONG NAME AND ARTIST BEFORE INSERTING INTO DB

# edge cases:
# - song/artist isn't found (in loop alr)
# - tags aren't found (in loop alr)
# - remove duplicates if found (built-in with sql)

# - incorporate a while loop with a counter so the loop stops when 100 songs are added
#     - just incase it skips songs that don't have a name or tags 


# def input_song()
#     users_song = 

# popular_genres = ['pop', 'hip-hop', 'hip hop', 'rap', 'rock', 'r&b', 'r and b', 'latin', 'edm', 'electronic',
#           'kpop', 'k-pop', 'korean pop', 'country', 'indie']

# # Retrieving 100 songs from each genre in list
# for genre in popular_genres:
params = {'tag': 'rap', 'limit': 100, 'api_key': api_key, 'method': 'tag.getTopTracks', 'format': 'json'}
request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
if request.status_code == 200:
    data = request.json()
    tracks = data['tracks']['track']
    for t in tracks:
        song_name = t.get('name')
        artist_name = t.get('artist', {}).get('name')
        if song_name and artist_name:
            params = {'track': song_name, 'artist': artist_name, 'api_key': api_key, 'method': 'track.getTopTags', 'format': 'json'}
            request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
        else:
            continue
        if request.status_code == 200:
            data = request.json()
            tags = data['toptags']['tag']
            tags_list = []
            for t in tags:
                tag = t.get('name')
                if tag:
                    tags_list.append(tag)
                    # OR would i not need a list. could it just add each one iteratively


# # Connecting to SQL
# connection = sqlite3.connect('music_rec_schema')
# cursor = connection.cursor()

# THIS IS FOR TESTING FUNCTION OUTPUT

# params = {'tag': 'rock', 'limit': 100, 'api_key': api_key, 'method': 'tag.getTopTracks', 'format': 'json'}
# request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
# if request.status_code == 200:
#     data = request.json()
#     print(json.dumps(data, indent=1))
# else:
#     print(f"Error: {request.status_code}")

# song name = name
# artist = artist[name]