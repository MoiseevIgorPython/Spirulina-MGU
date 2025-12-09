import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent
MEDIA = BASE_DIR / 'media'
MEDIA.mkdir(parents=True, exist_ok=True)


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')  # или 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True  # для порта 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
    MAIL_DEBUG = False

a=Config()
print('=====================')
print(a.MAIL_USERNAME)
print(a.SQLALCHEMY_DATABASE_URI)
print(a.SECRET_KEY)
print(a.MAIL_SERVER)
print(a.MAIL_PORT)
print(a.MAIL_USE_TLS)
print(a.MAIL_USE_SSL)
print(a.MAIL_USERNAME)
print(a.MAIL_PASSWORD)
print(a.MAIL_DEFAULT_SENDER)
print(a.MAIL_DEBUG)
print('=====================')