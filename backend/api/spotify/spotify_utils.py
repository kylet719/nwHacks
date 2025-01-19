import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

def get_spotify_client():
    """Initialize and return a Spotify client using credentials from .env"""
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def find_spotify_tracks(songs_list):
    """
    Find Spotify track IDs for a list of songs
    
    Args:
        songs_list (list): List of dictionaries containing 'title' and 'artist'
                          Example: [{'title': 'Shape of You', 'artist': 'Ed Sheeran'}]
    
    Returns:
        list: List of dictionaries containing original song info and Spotify track ID
              Returns None for track_id if no match is found
    """
    sp = get_spotify_client()
    results = []
    
    for song in songs_list:
        # Create search query combining title and artist
        query = f"track:{song['title']} artist:{song['artist']}"
        
        # Search Spotify
        response = sp.search(q=query, type='track', limit=1)
        
        # Extract track ID if found
        track_id = None
        if response['tracks']['items']:
            track_id = response['tracks']['items'][0]['id']
            
        # Add result to list
        results.append({
            'title': song['title'],
            'artist': song['artist'],
            'spotify_track_id': track_id
        })
    
    return results

def create_playlist_test():
    songs = [
        {'title': 'Blinding Lights', 'artist': 'The Weeknd'},
        {'title': 'Shape of You (Deluxe)', 'artist': 'Ed Sheeran'},
        {'title': 'Tweaker', 'artist': 'Gelo'},
        {'title': 'Streetcar', 'artist': 'Daniel Caesar'},
    ]

    sp = get_spotify_client()
    user_info = sp.current_user()
    print(user_info)

    spotify_results = find_spotify_tracks(songs)

    for result in spotify_results:
        print(f"Song: {result['title']} - {result['artist']}")
        print(f"Spotify ID: {result['spotify_track_id']}\n")

    # Example: Get user info
    user_info = sp.current_user()
      
    # Example: Create a playlist
    playlist = sp.user_playlist_create(
        user_info['id'],
        "My Moodiest playlist 2",
        public=False,
        description="Generated based on mood"
    )

    # Add tracks to playlist
    track_ids = [result['spotify_track_id'] for result in spotify_results if result['spotify_track_id'] is not None]
    if track_ids:
        sp.playlist_add_items(playlist['id'], track_ids)

    print("DONE")