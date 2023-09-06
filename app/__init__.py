import os

import spotipy
import spotipy.util as sp_util  # Import Spotify utility functions
from config import Config
from flask import (Flask, redirect, render_template, request,
                   session, url_for)
from flask_session import Session
from spotipy.oauth2 import SpotifyOAuth


# Initialize and configure Flask-Session
session = Session()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure Flask-Session
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False
    session.init_app(app)
    return app


app = create_app()
from app.routes import *
