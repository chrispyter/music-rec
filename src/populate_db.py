#FROM EACH TAG IN TAG LIST:
#        FIND TOP TRACKS WITH THAT TAG
 #       FOR EACH TRACK ADDED TO DB:
#            GET THE TOP 10 TAGS
 #           ADD TAGS TO TAG LIST

import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
api_key = os.getenv("Last_fm_API_Key")

popular_genres = ['pop', 'hip-hop', 'hip hop', 'rap', 'rock', 'r&b', 'r and b', 'latin', 'edm', 'electronic',
          'kpop', 'k-pop', 'korean pop', 'country', 'indie', 'alternative']

# Retrieving 100 songs from each genre and adding to database
for genre in popular_genres:
    params = {'tag': genre, 'limit': 100, 'api_key': api_key, 'method': 'tag.getTopTracks', 'format': 'json'}
    request = requests.get("http://ws.audioscrobbler.com/2.0", params=params)
    if request.status_code == 200:
        data = request.json()
        print(json.dumps(data, indent=1))
    else:  
        print(f"Error: {request.status_code}")

# NEXT STEPS:
# Clean up output
# Make sure it's 100 songs for each genre
# Integrate with SQL


# Retrieve tags from songs added to database