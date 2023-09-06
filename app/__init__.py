from flask import Flask
from config import Config
from flask_session import Session

# Initialize and configure Flask-Session
session = Session()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure Flask-Session
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False
    session.init_app(app)

    # Import and register routes
    from app import routes

    return app
