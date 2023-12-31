from flask import render_template, redirect, url_for, session, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as sp_util
import os

from app import app

# Define Spotify API credentials and settings
client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = 'http://localhost:5000/callback'
scope = 'user-library-read,user-top-read'

# Initialize SpotifyOAuth outside of any function
sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
        )

# Set this to False for production
SHOW_DIALOG = True

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
    refresh_token_if_expired(sp_oauth)

    # Initialize a Spotipy instance with the user's access token
    sp = spotipy.Spotify(auth=session['token_info']['access_token'])

    # Fetch the user's top tracks using Spotipy
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')

    # Implement your new recommendation logic here
    # For simplicity, let's just fetch some popular tracks
    recommended_tracks = sp.search(q='genre:"pop"', type='track', limit=10)

    # Pass both top_tracks and recommended_tracks to the recommendations template
    return render_template('recommendations.html', recommended_tracks=recommended_tracks, top_tracks=top_tracks)

def create_spotify_oauth():
    return sp_oauth

def refresh_token_if_expired(sp_oauth):
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
