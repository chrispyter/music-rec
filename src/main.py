# Imports enable API requests, formatted outputs, and retrieval of private credentials from 
# separate environment
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

# Testing a method call to identify potential errors with API key, overlooked parameters, etc.
params = {'artist': 'Future', 'limit': 5, 'api_key': api_key, 'method': 'artist.getSimilar', 'format': 'json'}
request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
if request.status_code == 200:
    data = request.json()
#   print(json.dumps(data, indent=1))
else:
    print(f"Error: {request.status_code}")

# Using getTopTags to identify commonly-used tags for a song, helpful for mood analysis
params = {'artist': 'John Lennon', 'track': 'Imagine', 'api_key': api_key, 'limit': 3, 'method': 'track.getTopTags', 'format': 'json'}
request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
if request.status_code == 200:
    data = request.json()
    print(json.dumps(data, indent=1))
else:
    print(f"Error: {request.status_code}")

# Testing iteration through a list of songs to automate retrieval of tags for each song
params = {'artist': 'Future', 'limit': 5, 'api_key': api_key, 'method': 'artist.getTopTags', 'format': 'json'}
song_list = [{'artist': 'John Lennon', 'track': 'Imagine'}, {'artist': 'Mac Miller', 
        'track': 'The Spins'}, {'artist': 'The Smashing Pumpkins', 'track': '1979'}]
for song in song_list:
    if request.status_code == 200:
        params['artist'] = song['artist']
        params['track'] = song['track']
        request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
        data = request.json()
        print(json.dumps(data, indent=1))
    else:  
        print(f"Error: {request.status_code}")