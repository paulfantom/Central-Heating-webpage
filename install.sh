#!/bin/bash
PASSWORD = "$1"

sudo apt-get install -y python-virtualenv libffi-dev python-dev

virtualenv venv
source venv/bin/activate
pip install flask{,-login,-wtf,-sqlalchemy,-babel,-bcrypt} wtforms sqlalchemy jinja2 pymysql paho-mqtt

ed -i -e "s/MYSQL_PASS = ''/MYSQL_PASS = '$PASSWORD'/" config.py
