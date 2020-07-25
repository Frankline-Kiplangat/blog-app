import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
     DEBUG = False
     TESTING = False
     QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
     SECRET_KEY = '1234'
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
     UPLOADED_PHOTOS_DEST='app/static/photos'
    
     

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig,
'production':ProductionConfig,
'development': DevelopmentConfig
}
