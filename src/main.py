# Import necessary modules
import os
from dotenv import load_dotenv
import json
import requests

# Load environment variables from the .env file
load_dotenv()

# Defining API key
api_key = os.getenv("Last_fm_API_Key")

# Setting up parameters for test call
params = {'artist': 'Future', 'limit': 5, 'api_key': api_key, 'method': 'artist.getSimilar', 'format': 'json'}

# Testing a method call
request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
if request.status_code == 200:
    data = request.json()
    print(json.dumps(data, indent=1))
else:
    print(f"Error: {request.status_code}")