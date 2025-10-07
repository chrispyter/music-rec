# Imports enable API requests, formatted outputs, and retrieval of private credentials 
# from separate environment
import os
from dotenv import load_dotenv
import json
import requests
import sqlite3

# Loading API key
load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

# Connecting to SQL
connection = sqlite3.connect('music_rec_schema')
cursor = connection.cursor()

# Gets song name input by user
song_name = input("Enter any song:")
artist_name = input("Enter the song's artist:")

cursor.execute("SELECT song_id FROM songs WHERE song_name = ? AND artist = ?", (song_name, artist_name))
result = cursor.fetchone()
if result:
    song_id = result[0]
    cursor.execute("SELECT tag FROM tags JOIN song_tags ON tags.tag_id = song_tags.tag_id WHERE song_id = ?", (song_id,))
    tags = cursor.fetchall()
else:
    print("Song not found in database. Please try another!")

# gets tags from input song
# find songs that share tags
# either:
#     - output 5 songs that share the most amount of tags
#     - score tags by importance rather than just werighing based on number of shared tags
#     - or use both scoring and number of tags

# edge cases:
# - no tags are found
# - song or artist is spelled differently
#     - already have this accounted for, but what about artists who have accents in their names or a mix of capital and lowercase letters, like Beyonce or PnB Rock

# questions:
# - other ways to tailor recommendations?
#     - qualities of songs such as tempo
# - could we also include an api call that gets top tags from the artist and recommends songs with some of those tags (probably from database)


# Handling edge cases for API request and input song errors
# params = {'track': song_name, 'artist': artist_name, 'limit': 10, 'api_key': api_key, 'method': 'track.getTopTags', 'format': 'json'}
# request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
# if request.status_code == 200:
#     data = request.json()
#     if 'error' in data:
#             print(f"{data['message']}. Did you spell the song's name and artist correctly?")
#     elif not data['toptags']['tag']:
#          print('No song information could be found. Try inputting a more popular artist!')
#     else: 
#         print(json.dumps(data['toptags']['tag'], indent=1))
# else:
#     print(f"API Request Error: {request.status_code}")