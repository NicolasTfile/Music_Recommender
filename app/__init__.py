from flask import Flask
from config import Config
from flask_session import Session  # Import Flask-Session
from app import routes  # Import your routes here

# Initialize and configure Flask-Session
session = Session()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure Flask-Session
    app.config['SESSION_TYPE'] = 'filesystem'  # Use the filesystem to store sessions
    app.config['SESSION_PERMANENT'] = False     # Sessions are not permanent (expire when the browser is closed)

    session.init_app(app)  # Initialize Flask-Session

    # Other imports and configurations

    # Register Blueprints and routes
    app.register_blueprint(routes.bp)

    return app
