from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from .settings import Config
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_basicauth import BasicAuth
from sqlalchemy.orm import DeclarativeBase
from flask_mail import Mail


load_dotenv()


class Base(DeclarativeBase):
    pass


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
# app.json.ensure_ascii = False

db = SQLAlchemy(app, model_class=Base)
migrate = Migrate(app, db)
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Залогиньтесь пожалуйста!!!"

# basic_auth = BasicAuth(app)
from . import models
from .admin import admin, admin_view
from .site import views
