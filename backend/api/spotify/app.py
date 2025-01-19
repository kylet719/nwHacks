from flask import Flask, request, url_for, session, redirect
from spotify_auth import create_spotify_oauth, get_spotify_client
from spotify_utils import get_spotify_client, find_spotify_tracks, create_playlist_test


app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a real secret key

@app.route('/')
def index():
   return '''
       <h1>Welcome to Mood Music</h1>
       <a href="/login">Login with Spotify</a>
   '''


@app.route('/login')
def login():
   # Create OAuth instance and get auth URL
   sp_oauth = create_spotify_oauth()
   auth_url = sp_oauth.get_authorize_url()
   print(f"Redirecting to Spotify auth URL: {auth_url}")  # Debug print
   return redirect(auth_url)


@app.route('/callback')
def callback():
   print("Callback received!")  # Debug print
   # Get access token and store in session
   sp_oauth = create_spotify_oauth()
   session.clear()
   code = request.args.get('code')
   token_info = sp_oauth.get_access_token(code)
   print(f"Received code: {code}")  # Debug print
   session["token_info"] = token_info
   return redirect('/playlist')

@app.route('/playlist')
def create_playlist():
   try:
       # Get Spotify client
       sp = get_spotify_client()

       test_mood = "angry"
       test_playlist_name = "mad list"

       create_playlist_test(test_mood, test_playlist_name)
      
       return f"Created playlist"
  
   except Exception as e:
       return f"Error: {str(e)}"


if __name__ == '__main__':
   app.run(port=8000, debug=True)


