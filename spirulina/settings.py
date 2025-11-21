import os
from pathlib import Path


BASE_DIR = Path(__file__).parent
MEDIA = BASE_DIR / 'media'
MEDIA.mkdir(parents=True, exist_ok=True)


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465  # или 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True  # для порта 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    MAIL_DEBUG = False
    