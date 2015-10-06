from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
from os import path
from config import BABEL_DEFAULT_LOCALE,SERVER_IP
import paho.mqtt.client as mqtt
#from app.mqtt import on_connect, on_message as on_connect, on_message
from mqtt import on_connect, on_message

SENSORS_DATA = {}

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

client = mqtt.Client()
#client.connect(SERVER_IP,1883,60)
client.connect('192.168.2.2',1883,60)
client.loop_start()
client.on_connect = on_connect
client.on_message = on_message
