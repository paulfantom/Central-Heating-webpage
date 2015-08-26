from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
from os import path
from config import BABEL_DEFAULT_LOCALE

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)
db = SQLAlchemy(app)
#from app import views
from app import views, models

# check if database exists
# if not create database
if not path.isfile(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///','')):
    print("Creating new Database")
    db.create_all()
    #and initialize with defaults
    db.session.add(models.Settings(30,30,50,4.5,40,7.7,4.3,130,71.2,55.3,39,0.3,
        '{"free":[["7:00","22:00",21]],"work":[["05:30","7:30",21],["15:00","21:00",21]],"other":18,"week":[0,0,0,0,0,1,1]}',
        22.1,True,1.5))
    db.session.commit()


