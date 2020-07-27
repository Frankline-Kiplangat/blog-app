import os
class Config:
    '''
    General configuration settings
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY =('SECTRE_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SECRET_KEY="testkeyindevconfig"
    # SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:1234@localhost/myblog"
    DEBUG = True

class TestConfig(Config):
    SECRET_KEY="testkeyintestconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:1234@localhost/myblog_test"

configurations = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
}