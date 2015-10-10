# -*- coding: UTF-8 -*-

import os
from flask.ext.babel import gettext
basedir = os.path.abspath(os.path.dirname(__file__))

MQTT_ID = 'webclient'
SERVER_IP = "127.0.0.1"
MYSQL_USER = 'mqttwarn'
MYSQL_PASS = ''

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + MYSQL_USER + ':' + MYSQL_PASS + '@localhost/mqtt_data'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

LANGUAGES = {
    'en': 'English',
    'pl': 'Polski'
}

BABEL_DEFAULT_LOCALE = 'pl'

DESCRIPTIONS = {
    'circulation': {
        'interval' : {
            'title' : gettext('Interval'),
            'desc'  : gettext('Set pump interval in water consumption mode'),
            'range' : [1,180],
            'unit'  : ' min'
        },
        'time_on' : {
            'title' : gettext('ON time'),
            'desc'  : gettext('Set pump mixing time in water consumption mode'),
            'range' : [1,300],
            'unit'  : ' s'
        }},
    'heater' : {
        'critical' : {
            'title' : gettext('Critical'),
            'desc'  : gettext('Set heater critical temperature'),
            'range' : [40,100],
            'step'  : 1,
            'unit'  : u'°C'
        },
        'hysteresis' : {
            'title' : gettext('Hysteresis'),
            'desc'  : gettext('Set heater hysteresis for central heating'),
            'range' : [0,2],
            'step'  : 0.01,
            'unit'  : u'°C'
        }},
    'solar': {
        'temp_off' : {
            'title' : gettext('Temperature difference (OFF)'),
            'desc'  : gettext('Temperature difference needed to stop solar system'),
            'range' : [0.1,15],
            'step'  : 0.1,
            'unit'  : u'°C'
        },
        'temp_on'  : {
            'title' : gettext('Temperature difference (ON)'),
            'desc'  : gettext('Temperature difference needed to start solar system'),
            'range' : [0.1,15],
            'step'  : 0.1,
            'unit'  : u'°C'
        },
        'critical' : {
            'title' : gettext('Critical temperature'),
            'desc'  : gettext('Temperature of solar system turning off'),
            'range' : [80,200],
            'unit'  : u'°C'
        }},
    'tank' : {
        'solar_max'  : {
            'title' : gettext('Solar'),
            'desc'  : gettext('DHW maximum temperature with solar system usage'),
            'range' : [30,100],
            'unit'  : u'°C'
        },
        'heater_max' : {
            'title' : gettext('Heater (max)'),
            'desc'  : gettext('DHW maximum temperature with heater system usage'),
            'range' : [30,90],
            'unit'  : u'°C'
        },
        'heater_min' : {
            'title' : gettext('Heater (min)'),
            'desc'  : gettext('DHW minimum temperature with heater system usage'),
            'range' : [20,60],
            'unit'  : u'°C'
        }},

    'schedule' : {
        'override_temp': {
            'title' : gettext('Room temperature'),
            'desc'  : gettext('Override scheduled room temperature for 1 hour'),
            'range' : [15,28],
            'step'  : 0.1,
            'unit'  : u'°C'
        }}
}
