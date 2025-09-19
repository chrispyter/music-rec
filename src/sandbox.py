import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

# # Testing a method call to identify potential errors with API key, overlooked parameters, etc.
# params = {'artist': 'Future', 'limit': 5, 'api_key': api_key, 'method': 'artist.getSimilar', 'format': 'json'}
# request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
# if request.status_code == 200:
#     data = request.json()
# #   print(json.dumps(data, indent=1))
# else:
#     print(f"Error: {request.status_code}")

# # Hardcoded parameters for track.getTopTags method to evaluate its output
# params = {'artist': 'John Lennon', 'track': 'Imagine', 'api_key': api_key, 'limit': 10, 'method': 'track.getTopTags', 'format': 'json'}
# request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
# if request.status_code == 200:
#     data = request.json()
# #   print(json.dumps(data, indent=1))
# else:
#     print(f"Error: {request.status_code}")

# # Automating the retrieval of tags for songs to understand the kind of language used for tags
# params = {'artist': 'Future', 'limit': 5, 'api_key': api_key, 'method': 'artist.getTopTags', 'format': 'json'}
# song_list = [{'artist': 'John Lennon', 'track': 'Imagine'}, {'artist': 'Mac Miller', 
#         'track': 'The Spins'}, {'artist': 'The Smashing Pumpkins', 'track': '1979'}]
# for song in song_list:
#     if request.status_code == 200:
#         params['artist'] = song['artist']
#         params['track'] = song['track']
#         request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
#         data = request.json()
#    #    print(json.dumps(data, indent=1))
#     else:  
#         print(f"Error: {request.status_code}")

# Checking to see how many songs were output for each genre in my database 
# population script
popular_genres = ['pop', 'hip-hop', 'hip hop', 'rap', 'rock', 'r&b', 'r and b', 'latin', 'edm', 'electronic', 'kpop', 'k-pop', 'korean pop', 'country', 'indie']
with open('test.out', 'r') as file:
    first_genre = True
    genre_index = 0
    count = 0
    for line in file:
        if line.startswith('Song 1:'):
            if not first_genre:
                print(f'Genre: {popular_genres[genre_index]} Song Count: {count}')
                genre_index += 1
            else:
                first_genre = False
            count = 1
        else:
            count += 1
    print(f'Genre: {popular_genres[genre_index]} Song Count: {count}')