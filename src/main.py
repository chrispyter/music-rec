# Imports enable API requests, formatted outputs, and retrieval of private credentials from 
# separate environment
import os
from dotenv import load_dotenv
import json
import requests
import sqlite3

load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

# Gets song name input by user
song_name = input("Enter any song:")
artist_name = input("Enter the song's artist:")

# Handling edge cases for API request and input song errors
params = {'track': song_name, 'artist': artist_name, 'limit': 10, 'api_key': api_key, 'method': 'track.getTopTags', 'format': 'json'}
request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
if request.status_code == 200:
    data = request.json()
    if 'error' in data:
            print(f"{data['message']}. Did you spell the song's name and artist correctly?")
    elif not data['toptags']['tag']:
         print('No song information could be found. Try inputting a more popular artist!')
    else: 
        print(json.dumps(data['toptags']['tag'], indent=1))
else:
    print(f"API Request Error: {request.status_code}")

# Getting songs that share tags of the input song to gauge similarity (in progress)
def get_track_top_tags(artist, track, limit=10):
    params = {'artist': artist, 'track': track, 'api_key': api_key, 'limit': limit, 'method': 'track.getTopTags', 'format': 'json'}
    request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
    if request.status_code == 200:
        data = request.json()
        print(json.dumps(data, indent=1))
    else:
        print(f"Error: {request.status_code}")