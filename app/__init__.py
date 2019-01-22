from flask import *
from app.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.secret_key = 'please give me a good grade'
db = SQLAlchemy(app)
login = LoginManager(app)

from app import routes