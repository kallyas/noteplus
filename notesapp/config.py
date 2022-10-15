# This file contains the configuration for the flask application
# for various environments

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

UPLOAD_FOLDER = os.path.abspath(os.path.dirname('uploads'))
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# Base configuration
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
    UPLOAD_FOLDER = UPLOAD_FOLDER
    ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS
    # MAIL_HOST = os.environ['MAIL_HOST']
    # MAIL_PORT = os.environ['MAIL_PORT']
    # MAIL_USERNAME = os.environ['MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = False

# Development configuration
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# Testing configuration
class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///notesapp.db'

# Production configuration
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL_PRODUCTION']


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}