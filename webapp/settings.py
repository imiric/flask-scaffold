class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    APP_NAME = 'Webapp'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
