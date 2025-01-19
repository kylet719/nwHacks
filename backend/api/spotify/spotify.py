import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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

# Example usage:
if __name__ == "__main__":


    songs = [
        {'title': 'Shape of You', 'artist': 'Ed Sheeran'},
        {'title': 'Blinding Lights', 'artist': 'The Weeknd'},
        {'title': 'Shape of You (Deluxe)', 'artist': 'Ed Sheeran'},
    ]


    spotify_results = find_spotify_tracks(songs)

    for result in spotify_results:
        print(f"Song: {result['title']} - {result['artist']}")
        print(f"Spotify ID: {result['spotify_track_id']}\n")

    # Now for each ID, I want to create a playlist using the user's account. 
