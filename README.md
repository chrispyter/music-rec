# Title: 
Music Recommendation Algorithm

# Project Motive and Description:
Since this is my first coding project, I wanted to create something that aligns with one of my interests. I love listening to music and exploring new genres and artists. However, it can be difficult and time consuming to find new music, especially when I've listened to the majority of my favorite artists' discography. This project will allow me to discover new music by analyzing several features of a song or songs that I input into my algorithm. From this analysis, the algorithm will output several songs that share similar features to the input song or songs. From this, I can expand my music library and easily find new artists and songs that I enjoy. This will also enable other people viewing this project (like you!) to find new music.

# Planned Features (get rid of 'planned' part when publishing to GitHub):
- Suggest 10 songs similar to an input song or songs based on a combination of similar features (REQUIRED)
- Suggest 10 songs that have a similar feature to an input song or songs, such as the kind of beat, flow of lyrics, energy the song outputs, etc. (NICE TO HAVE)
- Suggest 10 songs that align with the user's mood, which is input by the user (NICE TO HAVE)
- Suggest 10 songs that align with an environment, which is input by the user (NICE TO HAVE)
    - Examples of an environment: fancy restaurant, house party, road trip, family barbeque, etc.

# Setup Instructions & Usage:
Follow these steps to set up the project locally.

1. Clone the repository:
- git clone INSERT GIT-LINK
- cd REPO-NAME

2. Create a virtual environment:
- python3 -m venv .venv

3. Activate the virtual environment: 
- On macOS/Linux:
    - source .venv/bin/activate
- On Windows:
    - .venv\Scripts\activate

4. Install the dependencies:
- pip install -r requirements.txt

5. Set up the environment variables:
- Last_fm_API_Key=YOUR_API_KEY_HERE
- Last_fm_Shared_Secret=YOUR_SHARED_SECRET_HERE
- Last_fm_Callback_URL=YOUR_CALLBACK_URL (Last.fm recommended: https://127.0.0.1:8888/callback)