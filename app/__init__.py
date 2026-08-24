from flask import Flask
from app.config import config
from flask_cors import CORS


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    #  enregistrement des blueprints
    from app.routes import audio_bp
    app.register_blueprint(audio_bp)  
    return app
