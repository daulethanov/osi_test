import os
from datetime import timedelta
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATION")
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    JWT_SECRET_KEY = "secret_jwt"
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'aliz1233773@gmail.com'
    MAIL_PASSWORD = 'rqqkbhzwhmqesfcx'
    MAIL_DEFAULT_SENDER = 'aliz1233773@gmail.com'