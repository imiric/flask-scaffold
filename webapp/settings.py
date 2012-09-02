class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    APP_NAME = 'Webapp'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://webapp:webapp@localhost:5432/webapp'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///webapp.db'

class TestingConfig(Config):
    TESTING = True
