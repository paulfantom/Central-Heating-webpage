#!/bin/bash
PASSWORD="$1"

if [ $(id -u) -eq 0 ]; then
  SUDO=""
else
  SUDO="sudo"
fi

eval $SUDO apt-get install -y python-virtualenv libffi-dev python-dev

virtualenv venv
source venv/bin/activate
pip install flask{,-login,-wtf,-sqlalchemy,-babel,-bcrypt} wtforms sqlalchemy jinja2 pymysql paho-mqtt

RANDOM_KEY=$(tr -cd '[:alnum:]' < /dev/urandom | fold -w32 | head -n1)
sed -i -e "s/MYSQL_PASS = ''/MYSQL_PASS = '$PASSWORD'/" config.py
sed -i -e "s/SECRET_KEY = 'you-will-never-guess'/SECRET_KEY = '$RANDOM_KEY'/" config.py

deactivate
exit 0
