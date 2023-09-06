from flask import render_template, redirect, url_for, session, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as sp_util
import os
from app import create_app  # Import create_app function

app = create_app()  # Initialize the Flask app

# Define Spotify API credentials and settings
client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = 'http://localhost:5000/callback'
scope = 'user-library-read,user-top-read'

# Set this to False for production
SHOW_DIALOG = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback/')
def callback():
    sp_oauth = create_spotify_oauth()
    session.clear()
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('recommendations'))

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if 'token_info' not in session:
        return redirect(url_for('login'))

    # Refresh the access token if it has expired
    refresh_token_if_expired()

    # Initialize a Spotipy instance with the user's access token
    sp = spotipy.Spotify(auth=session['token_info']['access_token'])

    # Fetch the user's top tracks using Spotipy
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')

    # Implement your content-based recommendation logic here
    # For simplicity, let's recommend tracks with similar genres to the user's top tracks
    recommended_tracks = []

    # Collect the genres of the user's top tracks
    user_top_genres = set()
    for track in top_tracks['items']:
        user_top_genres.update(track['artists'][0]['genres'])  # Assuming the first artist represents the track's genre

    # Fetch tracks based on similar genres
    for genre in user_top_genres:
        tracks_by_genre = sp.search(q=f'genre:"{genre}"', type='track', limit=5)
        recommended_tracks.extend(tracks_by_genre['tracks']['items'])

    # Pass both top_tracks and recommended_tracks to the recommendations template
    return render_template('recommendations.html', recommended_tracks=recommended_tracks, top_tracks=top_tracks)

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    )

def refresh_token_if_expired():
    token_info = session['token_info']
    if sp_oauth.is_token_expired(token_info):
        # Refresh the access token using the Spotify utility function
        sp_oauth = spotipy.oauth2.SpotifyOAuth(
                username=None,  # Automatically uses the username from the token_info
                scope=sp_oauth.scope,
                client_id=sp_oauth.client_id,
                client_secret=sp_oauth.client_secret,
                redirect_uri=sp_oauth.redirect_uri,
                cache_path=None  # Disable caching for simplicity
                )
        token_info = sp_oauth.refresh_access_token(session['token_info']['refresh_token'])
        session['token_info'] = token_info
