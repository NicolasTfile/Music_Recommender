import os

class Config:
    # Secret key for session management and security (change this to a secure value)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Spotify API configuration
    SPOTIFY_CLIENT_ID = 'd3cbb6dd842440e2bf48d4d316966a32'
    SPOTIFY_CLIENT_SECRET = 'a89d9230c20a4a099a0992b40c0e986c'
    SPOTIFY_REDIRECT_URI = 'http://localhost:5000/callback'
    SCOPE = 'user-library-read user-top-read'

    # SQLAlchemy database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use SQLite as an example
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Spotify API endpoint URLs
    SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1/'
    SPOTIFY_AUTH_BASE_URL = 'https://accounts.spotify.com/authorize'
    SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

    # Session configuration
    PERMANENT_SESSION_LIFETIME = 1800
    # Session lifetime in seconds (30 minutes)
