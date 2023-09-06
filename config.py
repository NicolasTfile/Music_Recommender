import os

class Config(object):
    # Secret key for session management and security (change this to a secure value)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Spotify API configuration
    SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback'
    SCOPE = 'user-library-read user-top-read'

    # Session configuration
    PERMANENT_SESSION_LIFETIME = 1800

    # Spotify API endpoint URLs
    SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1/'
    SPOTIFY_AUTH_BASE_URL = 'https://accounts.spotify.com/authorize'
    SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
