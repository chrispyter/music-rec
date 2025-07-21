# Imports enable API requests, formatted outputs, and retrieval of private credentials from 
# separate environment
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

# Getting songs that share tags of the input song to gauge similarity (in progress)
def get_track_top_tags(artist, track, limit=10):
    params = {'artist': artist, 'track': track, 'api_key': api_key, 'limit': limit, 'method': 'track.getTopTags', 'format': 'json'}
    request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
    if request.status_code == 200:
        data = request.json()
        print(json.dumps(data, indent=1))
    else:
        print(f"Error: {request.status_code}")

# IN PROGRESS (may get rid of due to new script integrating SQL)
tags = []
for tag in data['toptags']['tag']:
    if tag['name']:
        tags.append(tag['name'])
print(tags)