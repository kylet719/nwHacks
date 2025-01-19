from flask import Flask, request, url_for, session, redirect, render_template
from spotify_auth import create_spotify_oauth, get_spotify_client


# Initialize Flask with custom template and static folders
app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a real secret key


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Create OAuth instance and get auth URL
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    print(f"Redirecting to Spotify auth URL: {auth_url}")  
    return redirect(auth_url)

@app.route('/callback')
def callback():
    print("Callback received!")  
    # Get access token and store in session
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    print(f"Received code: {code}")  
    session["token_info"] = token_info
    return redirect('/playlist')

@app.route('/playlist')
def create_playlist():
    try:
        # Get Spotify client
        sp = get_spotify_client()
        
        # Example: Get user info
        user_info = sp.current_user()
        
        # Example: Create a playlist
        playlist = sp.user_playlist_create(
            user_info['id'],
            "My Mood Playlist",
            public=False,
            description="Generated based on mood"
        )
        
        return f"Created playlist: {playlist['name']}"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(port=8000, debug=True)