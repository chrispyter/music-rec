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
song_name = input("Enter a song name: ")
artist_name = input("Enter the song's artist(s): ")

# Function to retrieve input song tags, making it easier to reuse, debug, and
# improve code as needed
def get_top_song_tags(song_name, artist_name):
    params = {'track': song_name, 'artist': artist_name, 'limit': 10, 'api_key': api_key, 'method': 'track.getTopTags', 'format': 'json'}
    request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
    if request.status_code == 200:
        data = request.json()
        if 'error' in data:
            print(f"{data['message']}. Did you spell the song's name and artist correctly?")
            return None
        elif not data['toptags']['tag']:
            print('No song information could be found. Try inputting a more popular song or artist!')
            return None
        else: 
            input_song_tags = (data['toptags']['tag'])
            return input_song_tags
    else:
        print(f"API Request Error: {request.status_code}")
        return None

# Algorithm to recommend songs
input_song_tags = get_top_song_tags(song_name, artist_name)
if input_song_tags is None:
    exit()
else:
    song_tags = [tag['name'] for tag in input_song_tags]
    cursor.execute('''SELECT song_id FROM songs 
                    WHERE song_name = ? AND artist_name = ?
                    ''', (song_name, artist_name))
    result = cursor.fetchone()
    input_song_id = result[0] if result else None
    if input_song_id is None:
        cursor.execute('''SELECT song_name, artist_name, COUNT(*) as shared_tag_count 
                       FROM songs 
                       JOIN song_tags ON songs.song_id = song_tags.song_id
						JOIN tags ON tags.tag_id = song_tags.tag_id
						WHERE tags.tag IN ({})
						GROUP BY song_name, artist_name
						HAVING shared_tag_count >= 3
						ORDER BY shared_tag_count DESC
                        LIMIT 20'''.format(','.join('?' * len(song_tags))), song_tags)
    else:
        cursor.execute('''SELECT song_name, artist_name, COUNT(*) as shared_tag_count FROM songs 
                        JOIN song_tags ON songs.song_id = song_tags.song_id
                        JOIN tags ON tags.tag_id = song_tags.tag_id
                        WHERE tags.tag IN ({}) AND songs.song_id != ?
                        GROUP BY song_name, artist_name
                        HAVING shared_tag_count >= 3
                        ORDER BY shared_tag_count DESC
                        LIMIT 20'''.format(','.join('?' * len(song_tags))), 
                        song_tags + [input_song_id])
    sim_tag_songs = cursor.fetchall()
    revised_list_sim_tag_songs = []
    artist_count = 0
    for sim_song in sim_tag_songs:
        recommended_song_name = sim_song[0]
        recommended_artist_name = sim_song[1]
        if recommended_artist_name == artist_name:
            if artist_count < 2:
                artist_count += 1
                revised_list_sim_tag_songs.append(recommended_song_name)
        else:
            revised_list_sim_tag_songs.append(recommended_song_name)
        if len(revised_list_sim_tag_songs) == 5:
            break                                             

# Showing the recommendations
if revised_list_sim_tag_songs:
    print("\nTop recommendations:")
    for idx, song in enumerate(revised_list_sim_tag_songs, 1):
        print(f"{idx}. {song}")
else:
    print("\nNo recommendations found matching the criteria.")

# Debug output
# print(f"Input song in database: {input_song_id is not None}")
# print(f"Number of tags: {len(song_tags)}")
# print(f"Tags: {song_tags}")
# print(f"Number of matching songs found: {len(sim_tag_songs)}")