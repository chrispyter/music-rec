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
# song_name = input("Enter any song:")
# artist_name = input("Enter the song's artist:")

# Test values
song_name = "Runaway"
artist_name = "Kanye West"

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
    list_sim_tag_songs = [sim_song[0] for sim_song in sim_tag_songs]
    revised_list_sim_tag_songs = []
    for sim_song in list_sim_tag_songs:
        count = 0 
        while count <= 2:
            if sim_song['artist'] == artist_name:
                count += 1
                revised_list_sim_tag_songs.append(sim_song)
            else:
                continue
    
    
    # stop when it reaches 3

    # look at every song
    # once count reaches 3, stop adding songs that have the same artist                                              


    # Debug output
    print(f"Input song in database: {input_song_id is not None}")
    print(f"Number of tags: {len(song_tags)}")
    print(f"Tags: {song_tags}")
    print(f"Number of matching songs: {len(list_sim_tag_songs)}")
    print(f"Matching songs: {sim_tag_songs}")
    
    if len(list_sim_tag_songs) >= 3:
        print("\nTop 5 recommendations:")
        print(list_sim_tag_songs)
    else:
        print(f"\nOnly found {len(list_sim_tag_songs)} songs with >= 5 shared tags.")


# need to figure out how to find songs that are good to test the code on


# ALGORITHM IDEA
# Get input song's weighted tags (1 API call)
# Get top tracks from top 3 tags (3 API calls)
# Get tags for each candidate track (many API calls - this is the complex part)
# Score each track based on tag overlap with weights
# Rank and return top 5


# edge cases:
# - no tags are found
# - song or artist is spelled differently
#     - already have this accounted for, but what about artists who have accents in their names or a mix of capital and lowercase letters, like Beyonce or PnB Rock