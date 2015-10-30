#!/bin/bash
sudo apt-get install -y python-virtualenv libffi-dev python-dev

virtualenv venv
source venv/bin/activate
pip install flask{,-login,-wtf,-sqlalchemy,-babel,-bcrypt} wtforms sqlalchemy jinja2 pymysql paho-mqtt
