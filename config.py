# -*- coding: UTF-8 -*-
from flask.ext.babel import lazy_gettext
import os
basedir = os.path.abspath(os.path.dirname(__file__))

MQTT_ID = 'webclient'
SERVER_IP = "127.0.0.1"
MYSQL_USER = 'mqttwarn'
MYSQL_PASS = ''

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + MYSQL_USER + ':' + MYSQL_PASS + '@localhost/mqtt_data'

BCRYPT_LOG_ROUNDS = 12

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

LANGUAGES = {
    'en': 'English',
    'pl': 'Polski'
}

BABEL_DEFAULT_LOCALE = 'pl'

WEEKDAYS = [lazy_gettext('Monday'),
            lazy_gettext('Tuesday'),
            lazy_gettext('Wednesday'),
            lazy_gettext('Thursday'),
            lazy_gettext('Friday'),
            lazy_gettext('Saturday'),
            lazy_gettext('Sunday')]

DESCRIPTIONS = {
    'circulation': {
        'interval' : {
            'title' : lazy_gettext('Interval'),
            'desc'  : lazy_gettext('Set pump interval in water consumption mode'),
            'range' : [1,180],
            'unit'  : ' min'
        },
        'time_on' : {
            'title' : lazy_gettext('ON time'),
            'desc'  : lazy_gettext('Set pump mixing time in water consumption mode'),
            'range' : [1,300],
            'unit'  : ' s'
        }},
    'heater' : {
        'expected': {
            'title' : lazy_gettext('Expected room temperature'),
            'desc'  : lazy_gettext('Override scheduled room temperature for 60 minutes'),
            'range' : [15,28],
            'step'  : 0.1,
            'unit'  : u'°C'
        },
        'critical' : {
            'title' : lazy_gettext('Critical'),
            'desc'  : lazy_gettext('Set heater critical temperature'),
            'range' : [40,100],
            'step'  : 1,
            'unit'  : u'°C'
        },
        'hysteresis' : {
            'title' : lazy_gettext('Hysteresis'),
            'desc'  : lazy_gettext('Set heater hysteresis for central heating'),
            'range' : [0,2],
            'step'  : 0.01,
            'unit'  : u'°C'
        }},
    'solar': {
        'temp_off' : {
            'title' : lazy_gettext('Temperature difference (OFF)'),
            'desc'  : lazy_gettext('Temperature difference needed to stop solar system'),
            'range' : [0.1,15],
            'step'  : 0.1,
            'unit'  : u'°C'
        },
        'temp_on'  : {
            'title' : lazy_gettext('Temperature difference (ON)'),
            'desc'  : lazy_gettext('Temperature difference needed to start solar system'),
            'range' : [0.1,15],
            'step'  : 0.1,
            'unit'  : u'°C'
        },
        'critical' : {
            'title' : lazy_gettext('Critical temperature'),
            'desc'  : lazy_gettext('Temperature of solar system turning off'),
            'range' : [80,200],
            'unit'  : u'°C'
        }},
    'tank' : {
        'solar_max'  : {
            'title' : lazy_gettext('Solar'),
            'desc'  : lazy_gettext('DHW maximum temperature with solar system usage'),
            'range' : [30,100],
            'unit'  : u'°C'
        },
        'heater_max' : {
            'title' : lazy_gettext('Heater (max)'),
            'desc'  : lazy_gettext('DHW maximum temperature with heater system usage'),
            'range' : [30,90],
            'unit'  : u'°C'
        },
        'heater_min' : {
            'title' : lazy_gettext('Heater (min)'),
            'desc'  : lazy_gettext('DHW minimum temperature with heater system usage'),
            'range' : [20,60],
            'unit'  : u'°C'
        }},

    'schedule' : {
        'override_temp': {
            'title' : lazy_gettext('Room temperature'),
            'desc'  : lazy_gettext('Override scheduled room temperature for 1 hour'),
            'range' : [15,28],
            'step'  : 0.1,
            'unit'  : u'°C'
        }}
}
