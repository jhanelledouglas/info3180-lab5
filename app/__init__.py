from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def __init__(self, id, first_name, last_name,username, password):
    self.first_name = first_name
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.password = password

app.config.from_object(Config)
from app import views
