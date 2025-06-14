# Import necessary modules
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from the .env file
load_dotenv()

# Initialize Spotify API client with OAuth credentials from environment variables
spotify_api = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-library-read"
))

# Testing a search request
results = spotify_api.search(q="track:3D Outro artist:Lucki", type="track", limit=1)
print(results)

track_id = results["tracks"]["items"][0]
print(track_id)

#audio_features = spotify_api.audio_features(tracks=)