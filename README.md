# Music Recommendation System

## Project Motive and Description
As my first coding project, I wanted to build something aligned with one of my favorite interests, which is discovering new music and artists. While I love finding new songs, it can be difficult and time-consuming since I've listened to the majority of my favorite artists' discographies.

This project generates personalized song recommendations by identifying songs that share similar features with a user-provided track. It connects to the **Last.fm API**, which is a web service that provides crowdsourced music metadata, genres, and user-generated tags. The algorithm ranks songs based on the number of shared characteristics with the input song, allowing users (like you!) to easily expand their music library and discover new music.

## Features
- Tag-Based Recommendations: Suggests 5 similar songs based on shared features (referred to as "tags" by Last.fm).

- SQLite Database Integration: Caches track and tag relationships locally for fast retrieval.

- Interactive CLI: Prompts users for song inputs directly in the terminal.

## Setup Instructions & Usage
Follow the steps below to set up the project locally. All steps should be executed in your system terminal (Terminal on macOS/Linux, or Command Prompt/PowerShell on Windows) unless indicated otherwise.

#### 1. Clone the repository:
- `git clone https://github.com/chrispyter/music-rec`
- `cd music-rec`

#### 2. Create a virtual environment:
- `python3 -m venv .venv`
- `source .venv/bin/activate`

#### 3. Activate the virtual environment: 
- On macOS/Linux:
    - `source .venv/bin/activate`
- On Windows:
    - `.venv\Scripts\activate`

#### 4. Install the dependencies:
- `pip install -r requirements.txt`

#### 5. Set up the environment variables:
To run this application, you will need a free Last.fm API key:
1. Sign in or create a free account at [Last.fm](https://www.last.fm/).
2. Go to the [Last.fm API Account Creation Page](https://www.last.fm/api/account/create).
3. Fill in **Application Name** (e.g., `Music Rec Tool`) and **Application Description**. Leave **Callback URL**  and **Application Homepage** blank or set to `http://127.0.0.1:8888/callback`.
4. Click **Submit** to generate your **API Key** and **Shared Secret**.

Next, create a `.env` file in the project root directory from your terminal:
- **macOS/Linux:** `touch .env`
- **Windows:** `type nul > .env`

Open `.env` in VS Code or your text editor and add your Last.fm credentials:
```text
Last_fm_API_Key=YOUR__API_KEY_HERE
Last_fm_Shared_Secret=YOUR__SHARED_SECRET_HERE
Last_fm_Callback_URL=https://127.0.0.1:8888/callback
```

#### 6. Run the application:
- `python src/main.py`