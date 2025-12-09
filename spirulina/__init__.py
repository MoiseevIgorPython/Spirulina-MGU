from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from .settings import Config

load_dotenv()


class Base(DeclarativeBase):
    pass


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

db = SQLAlchemy(app, model_class=Base)
migrate = Migrate(app, db)
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Залогиньтесь пожалуйста!!!"

from . import models
from .admin import admin, admin_view
from .site import views
