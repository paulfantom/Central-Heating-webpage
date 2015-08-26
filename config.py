# -*- coding: UTF-8 -*-

import os
from flask.ext.babel import gettext
basedir = os.path.abspath(os.path.dirname(__file__))

SERVER_IP = "127.0.0.1"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

LANGUAGES = {
    'en': 'English',
    'pl': 'Polski'
}

BABEL_DEFAULT_LOCALE = 'pl'

DESCRIPTIONS = {
    'circulation_time_off'     : {
        'title' : gettext('OFF time'),
        'desc'  : gettext('Set pump off time in water consumption mode'),
        'range' : [1,180],
        'unit'  : ' min'
    },
    'circulation_time_on'      : {
        'title' : gettext('ON time'),
        'desc'  : gettext('Set pump mixing time in water consumption mode'),
        'range' : [1,300],
        'unit'  : ' s'
    },
    'circulation_solar'        : {
        'title' : gettext('Required solar temperature'),
        'desc'  : gettext('Set solar minimal temperature needed to start circulation'),
        'range' : [30,150],
        'unit'  : u'°C'
    },
    'circulation_hysteresis'   : {
        'title' : gettext('Hysteresis'),
        'desc'  : gettext('Set hysteresis for circulation pump'),
        'range' : [0.5,10],
        'unit'  : u'°C',
        'step'  : 0.5
    },
    'circulation_temp'         : {
        'title' : gettext('Work temperature'),
        'desc'  : gettext('Set circulation pump working temperature'),
        'range' : [30,90],
        'unit'  : u'°C'
    },
    'solar_off'                : {
        'title' : gettext('Temperature difference (OFF)'),
        'desc'  : gettext('Temperature difference needed to stop solar system'),
        'range' : [0.1,15],
        'step'  : 0.1,
        'unit'  : u'°C'
    },
    'solar_on'                 : {
        'title' : gettext('Temperature difference (ON)'),
        'desc'  : gettext('Temperature difference needed to start solar system'),
        'range' : [0.1,15],
        'step'  : 0.1,
        'unit'  : u'°C'
    },
    'solar_critical'           : {
        'title' : gettext('Critical temperature'),
        'desc'  : gettext('Temperature of solar system turning off'),
        'range' : [80,200],
        'unit'  : u'°C'
    },
    'tank_solar_max'           : {
        'title' : gettext('Solar'),
        'desc'  : gettext('DHW maximum temperature with solar system usage'),
        'range' : [30,100],
        'unit'  : u'°C'
    },
    'tank_heater_max'          : {
        'title' : gettext('Heater (max)'),
        'desc'  : gettext('DHW maximum temperature with heater system usage'),
        'range' : [30,90],
        'unit'  : u'°C'
    },
    'tank_heater_min'          : {
        'title' : gettext('Heater (min)'),
        'desc'  : gettext('DHW minimum temperature with heater system usage'),
        'range' : [20,60],
        'unit'  : u'°C'
    },
    'schedule_override_temp'   : {
        'title' : gettext('Room temperature'),
        'desc'  : gettext('Override scheduled room temperature for 1 hour'),
        'range' : [15,30],
        'step'  : 0.1,
        'unit'  : u'°C'
    },
    'schedule'                 : ''
}
