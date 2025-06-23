# Import necessary modules
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

# Initialize Spotify API client with OAuth credentials from environment variables
spotify_api = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-library-read user-read-private user-read-email"
))

# Testing a search request
results = spotify_api.search(q="track:Blinding Lights artist:The Weeknd", type="track", limit=1)

# Getting a track ID for a song
track_id = results["tracks"]["items"][0]["id"]

# Looking at the audio features of a song
song_features = spotify_api.audio_features(tracks=[track_id])
print(song_features)