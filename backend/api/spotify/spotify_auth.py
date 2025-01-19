import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()


def print_env_vars():
   print("Client ID:", os.getenv('SPOTIPY_CLIENT_ID'))
   print("Client Secret:", os.getenv('SPOTIPY_CLIENT_SECRET'))
   print("Redirect URI:", os.getenv('SPOTIPY_REDIRECT_URI'))




def create_spotify_oauth():
   return SpotifyOAuth(
       client_id=os.getenv('SPOTIPY_CLIENT_ID'),
       client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
       redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
       scope=[
           'user-library-read',
           'playlist-modify-public',
           'playlist-modify-private',
           'user-read-private',
           'user-read-email'
       ]
   )


def get_spotify_client():
   # This will handle the auth flow automatically
   sp = spotipy.Spotify(auth_manager=create_spotify_oauth())
   return sp


if __name__ == "__main__":
   print_env_vars()
