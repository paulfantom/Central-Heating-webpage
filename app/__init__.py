from flask import Flask
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)

from app import views