import os
import requests
import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'

def get_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(AUTH_URL,
                             headers=headers,
                             data=data)
    
    if response.status_code == 200:
        token_info = response.json()
        return token_info['access_token']
    else:
        raise Exception('Failed to authenticate')
    
def create_playlist(name = None):
    if name == None:
        now = dt.datetime.now()
        name = f'Emotion Playlist {now.strftime("%Y-%m-%d %H:%M:%S")}'

    
    
get_token()