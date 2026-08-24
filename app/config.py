import os
from datetime import timedelta

class Config:
    # Configuration de Base de l'application
    #  CLé de sessions
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # CORS
    CORS_HEADERS='Content-Type'
    
class DevelopmentConfig(Config):
    DEBUG=True
    
class ProductionConfig(Config):
    DEBUG=False
    
config={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
    