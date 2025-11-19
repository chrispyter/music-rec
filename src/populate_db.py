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

# Generating songs and tags from a pre-set list of popular genres to establish a 
# comprehensive dataset of songs that the algorithm can work off of
popular_genres = ['pop', 'hip-hop', 'hip hop', 'rap', 'rock', 'r&b', 'r and b', 'latin', 'spanish', 'latino', 'edm', 'electronic', 'kpop', 'k-pop', 'korean pop', 'country', 'bluegrass', 'americana', 'indie']
for genre in popular_genres:
    count = 0
    params = {'tag': genre, 'limit': 120, 'api_key': api_key, 'method': 'tag.getTopTracks', 'format': 'json'}
    request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
    if request.status_code == 200:
        data = request.json()
        tracks = data['tracks']['track']
        for trk in tracks:
            if count >= 100:
                break
            else:
                song_name = trk.get('name')
                artist_name = trk.get('artist', {}).get('name')
                if song_name and artist_name:
                    params = {'track': song_name, 'artist': artist_name, 'api_key': api_key, 'method': 'track.getTopTags', 'format': 'json'}
                    request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
                else:
                    continue
                if request.status_code == 200:
                    data = request.json()
                    tags = data.get('toptags')
                    if tags:
                        tags = tags.get('tag')
                        tags_list = []
                        for t in tags:
                            tag = t.get('name')
                            if tag and len(tags_list) < 10:
                                tag = tag.lower()
                                tags_list.append(tag)
                        if not tags_list: 
                            continue
                        count += 1
                        cursor.execute("INSERT OR IGNORE INTO songs (song_name, artist_name) VALUES (?, ?)", (song_name, artist_name,))
                        cursor.execute("SELECT song_id FROM songs WHERE song_name = ? AND artist_name = ?", (song_name, artist_name,))
                        song_id = cursor.fetchone()[0]
                        for t in tags_list:
                            cursor.execute("INSERT OR IGNORE INTO tags (tag) VALUES (?)", (t,))
                            cursor.execute("SELECT tag_id FROM tags WHERE tag = ?", (t,))
                            tag_id = cursor.fetchone()[0]
                            cursor.execute("INSERT OR IGNORE INTO song_tags (song_id, tag_id) VALUES (?, ?)", (song_id, tag_id,))
connection.commit()
connection.close()