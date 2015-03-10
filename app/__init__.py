from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)
db = SQLAlchemy(app)
# check if database exists
# if not create database
#db.create_all()
#and initialize with defaults
#db.session.add(Settings(30,30,50,4.5,40,7.7,4.3,130,71.2,55.3,39.3,0.3,"{}",22.1,True,1.5))
#db.session.commit()

#from app import views
from app import views, models