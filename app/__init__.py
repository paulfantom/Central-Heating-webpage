from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
from flask.ext.bcrypt import Bcrypt
from os import path
from config import BABEL_DEFAULT_LOCALE

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)
db = SQLAlchemy(app)
#db.Model.metadata.reflect(db.engine)
bcrypt = Bcrypt(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
from app.core import models
lm.anonymous_user = models.Anonymous
#lm.session_protection = "strong"
from app.core import views
from app.startup import startup
