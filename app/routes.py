from flask import Blueprint, render_template, redirect, url_for, session, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import util as sp_util  # Import Spotify utility functions

bp = Blueprint('main', __name__)

# Define Spotify API credentials and settings
client_id = 'd3cbb6dd842440e2bf48d4d316966a32'
client_secret = 'a89d9230c20a4a099a0992b40c0e986c'
redirect_uri = 'http://localhost:5000/callback'
scope = 'user-library-read user-top-read'

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/login')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@bp.route('/callback')
def callback():
    sp_oauth = create_spotify_oauth()
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('recommendations'))

@bp.route('/recommendations', methods=['GET', 'POST'])
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

    # For simplicity, let's just pass the recommended tracks to the recommendations template
    return render_template('recommendations.html', recommended_tracks=recommended_tracks)

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
    )

def refresh_token_if_expired():
    token_info = session['token_info']
    if sp_oauth.is_token_expired(token_info):
        # Refresh the access token using the Spotify utility function
        token_info = sp_util.prompt_for_user_token(
            username=None,  # Automatically uses the username from the token_info
            scope=sp_oauth.scope,
            client_id=sp_oauth.client_id,
            client_secret=sp_oauth.client_secret,
            redirect_uri=sp_oauth.redirect_uri,
            cache_path=None,  # Disable caching for simplicity
        )
        session['token_info'] = token_info
