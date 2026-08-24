from flask import Blueprint

audio_bp= Blueprint('audio',__name__,url_prefix='/api/')
from app.routes import audio