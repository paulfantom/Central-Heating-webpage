# -*- coding: UTF-8 -*-

from flask import render_template, redirect, request
from flask.ext.babel import gettext
from wtforms.validators import NumberRange
from app import app, babel
from .forms import RangeForm, OptionsForm
from config import LANGUAGES

def get_data():



    return data

def get_from_SQL(record,field):
    return None

def apparent(toggle=False):
    #get apparent temperature switch state from SQL
    apparent = True

    if toggle:
        apparent = not apparent

    return apparent

def reboot():
    return None

def reboot_mcu():
    return None


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for OpenID="%s", remember_me=%s' %
#              (form.openid.data, str(form.remember_me.data)))
#        return redirect('/dashboard')
#    return render_template('login.html', 
#                           title='Sign In',
#                           form=form,
#                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
@app.route('/dashboard')
def dashboard():

    user='admin'
    data = { "room_temp" : 20,
             "feel_temp" : 21,
             "humidity"  : 60,
             "out_temp"  : 19,
             "work_mode" : gettext('Normal'),
             "heater_status" : gettext('ON'),
             "solar_status"  : gettext('ON') }
    return render_template("content/dashboard.html",
                           active='dashboard',
                           title='',
                           user=user,
                           data=data)

#@app.route('/set-room-temp', methods=['GET', 'POST'])
def room_temp():
    # get those data from SQL(name):
    slider = {'min'   : 10,
              'max'   : 80,
              'value' : 17,
              'step'  : 0.1,
              'unit'  : u'°C'}
    description = {'title'  : gettext('Example modal'),
                   'info'   : gettext('move it'),
                   's_info' : gettext('Temperature') + ':',
                   'cancel' : gettext('Cancel'),
                   'submit' : gettext('Save')}


    form = RangeForm()
    from wtforms.validators import NumberRange
    form.slider.validate(form,[NumberRange(slider['min'],slider['max'])])

    if form.validate_on_submit():
        val = request.form['slider']
        print(val)
        return redirect('/')

    return render_template("forms/modal-range.html",action=request.path,slider=slider,desc=description,form=form)

@app.route('/status')
def status():
    values = {'sensors' : [
                  {'title'  : gettext('Solar temperature'),
                   'name'   : 'solar_temp',
                   'unit'   : u'°C',
                   'value'  : 100.0 },
                  {'title'  : gettext('Outside temperature'),
                   'name'   : 'outside_temp',
                   'unit'   : u'°C',
                   'value'  : 26.5 },
                  {'title'  : gettext('Inside temperature'),
                   'name'   : 'room_temp',
                   'unit'   : u'°C',
                   'value'  : 22.1 },
                  {'title'  : gettext('Apparent temperature'),
                   'name'   : 'apparent_temp',
                   'unit'   : u'°C',
                   'value'  : 23.1 },
                  {'title'  : gettext('Humidity'),
                   'name'   : 'humidity',
                   'unit'   : u'%',
                   'value'  : 50 }],
              'meters'  : {
                  'labels'  : {'temp_in'  : gettext('Input temperature'),
                               'temp_out' : gettext('Output temperature'),
                               'temp_diff': gettext('Temperature difference'),
                               'flow'     : gettext('Flow'),
                               'energy'   : gettext('Energy'),
                               'consume'  : gettext('Consumption')},
                  'order'   : ['temp_in','temp_out','temp_diff','flow','energy','consume'],
                  'units'   : [u'°C',    u'°C',     u'°C',      u'm³/h',u'kWh', u'???'],
                  'devices' : [{'title'    : gettext('Solar'),
                                'name'     : 'solar',
                                'temp_in'  : 40.1,
                                'temp_out' : 30.2,
                                'temp_diff': 0.9,
                                'flow'     : 10,
                                'energy'   : 314.1,
                                'consume'  : 10},
                               {'title'    : gettext('Tank'),
                                'name'     : 'tank',
                                'temp_in'  : 40.1,
                                'temp_out' : 30.2,
                                'temp_diff': 0.9,
                                'flow'     : 10,
                                'energy'   : 314.1,
                                'consume'  : 10},
                               {'title'    : gettext('Heater'),
                                'name'     : 'heater',
                                'temp_in'  : 40.1,
                                'temp_out' : 30.2,
                                'temp_diff': 0.9,
                                'flow'     : 10,
                                'energy'   : 314.1,
                                'consume'  : 10}]},
              'states'  : [
                  {'title'  : gettext('Burner'),
                   'name'    : 'burner',
                   'value' : 'ON' },
                  {'title'  : gettext('Heater pump'),
                   'name'    : 'heater_pump',
                   'value' : 'ON' },
                  {'title'  : gettext('Solar pump'),
                   'name'    : 'solar_pump',
                   'value' : 'ON' },
                  {'title'  : gettext('Solar system actuator'),
                   'name'    : 'solar_switch',
                   'value' : 'ON' },
                  {'title'  : gettext('DHW/CH actuator'),
                   'name'    : 'heater_switch',
                   'value' : gettext('DHW') } ]}
    title=gettext('Sensors data')
    return render_template("/content/status.html",
                           active='status',
                           data=values,
                           title=title)

@app.route('/scheme')
def scheme():
    values = {'solar_temp'    : 100.0,
              'outside_temp'  : 26.5,
              'room_temp'     : 22.1,
              'room_humidity' : 50,
              'apparent_temp' : 23.1,
              'solar_meter'   :
                  {'temp_in'  : 40.1,
                   'temp_out' : 30.2,
                   'temp_diff': 0.9,
                   'flow'     : 10,
                   'energy'   : 314.1,
                   'consume'  : 10},
              'heater_meter'  :
                  {'temp_in'  : 40.1,
                   'temp_out' : 30.2,
                   'temp_diff': 0.9,
                   'flow'     : 10,
                   'energy'   : 314.1,
                   'consume'  : 10},
              'tank_meter'    :
                  {'temp_in'  : 40.1,
                   'temp_out' : 30.2,
                   'temp_diff': 0.9,
                   'flow'     : 10,
                   'energy'   : 314.1,
                   'consume'  : 10},
              'state'         :
                  {'burner'       : False,
                   'heater_pump'  : False,
                   'solar_pump'   : False,
                   'solar_switch' : False,
                   'heater_switch': False}}
    return render_template("/content/scheme.html",active='scheme',data=values)

@app.route('/water/')
def water():
    values = [ {'title' : gettext('Current temperature'),
                'value' : 44 },
               {'name'  : "solar_max",
                'value' : 90,
                'range' : [30,100],
                'title' : gettext('Solar'),
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z kolektora' },
               {'name'  : "heater_max",
                'value' : 90,
                'range' : [30,100],
                'title' : gettext('Heater (max)'),
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z pieca' },
               {'name'  : "heater_min",
                'value' : 30,
                'range' : [30,100],
                'title' : gettext('Heater (min)'),
                'desc'  : u'Ustaw minimalną temperaturę wody w zbiorniku dla zasilania z pieca' }]

    return render_template("data_rows.html",
                           active='water',
                           data=values,
                           title=gettext('Water'))

@app.route('/circulation/')
def circulation():
    values = [ {'name'  : "circulation_temp",
                'value' : 40,
                'range' : [30,100],
                'unit'  : u'°C',
                'title' : gettext('Work temperature'),
                'desc'  : u'Ustaw temperaturę pracy pompy cyrkulacyjnej' },
               {'name'  : "circulation_hyst",
                'value' : 4,
                'range' : [0.5,10],
                'step'  : 0.5,
                'unit'  : u'°C',
                'title' : gettext('Hysteresis'),
                'desc'  : u'Ustaw histerezę pracy pompy cyrkulacyjnej' },
               {'name'  : "circulation_solar",
                'value' : 70,
                'range' : [30,150],
                'unit'  : u'°C',
                'title' : gettext('Required solar temperature'),
                'desc'  : u'Ustaw minimalną temperaturę kolektora dla załączenia cyrkulacji' },
               {'name'  : "time_on",
                'value' : 30,
                'range' : [1,300],
                'unit'  : 's',
                'title' : gettext('ON time'),
                'desc'  : u'Ustaw czas pracy pompy w trybie poboru wody' },
               {'name'  : "time_off",
                'value' : 30,
                'range' : [1,180],
                'unit'  : ' min',
                'title' : gettext('OFF time'),
                'desc'  : u'Ustaw przerwę w pracy pompy w trybie poboru wody' } ]
    return render_template("data_rows.html",
                           active='circulation',
                           data=values,
                           title=gettext('Circulation'))

@app.route('/heater')
def heater():
    values = [{'title' : gettext('Work day'),
               'id'    : 'work_day',
               'table' : {
                   'title'     : gettext('Heating schedule'),
                   'col_names' : [gettext('FROM'),gettext('TO'),u'T [°C]'],
                   'data'      : [['10:00','20:23',21],['23:01','23:59',20]],
                   'footer'    : [gettext('Other'),gettext('Hours'),18]}},
              {'title' : gettext('Free day'),
               'id'    : 'free_day',
               'table' : {
                   'title'     : gettext('Heating schedule'),
                   'col_names' : ['OD','DO',u'T [°C]'],
                   'data'      : [['06:00','12:23',21],['15:01','23:59',20]],
                   'footer'    : [gettext('Other'),gettext('Hours'),16]}},
              {'title' : gettext('Week'),
               'id'    : 'week',
               'data'  : [
                   {'id' : 'mon', 'name' : gettext('Monday'), 'state' : False},
                   {'id' : 'tue', 'name' : gettext('Tuesday'), 'state' : False},
                   {'id' : 'wed', 'name' : gettext('Wednesday'), 'state' : False},
                   {'id' : 'thu', 'name' : gettext('Thursday'), 'state' : False},
                   {'id' : 'fri', 'name' : gettext('Friday'), 'state' : False},
                   {'id' : 'sat', 'name' : gettext('Saturday'), 'state' : True},
                   {'id' : 'sun', 'name' : gettext('Sunday'), 'state' : True} ]}
               ]

    hyst = 0.5

    return render_template("content/heater.html",
                           active='heater',
                           tabs=values,
                           hysteresis_value=hyst,
                           save=True,
                           title=gettext('Heater'))

@app.route('/solar/')
def solar():
    user = request.args.get('t')
    if user is not None:
        title=user
    else:
        title="Solar"

    values = [ {'title' : gettext('Current temperature'),
                'value' : 10 },
               {'name'  : "solar_critical",
                'value' : 130,
                'range' : [70,200],
                'unit'  : u'°C',
                'title' : gettext('Critical temperature'),
                'desc'  : u'Ustaw krytyczną temperaturę wyłączenia kolektora' },
               {'name'  : "solar_tank",
                'value' : 90,
                'range' : [0.5,10],
                'step'  : 0.1,
                'unit'  : u'°C',
                'title' : gettext('Water temperature'),
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z kolektora' },
               {'name'  : "solar_on",
                'value' : 4,
                'range' : [0.5,15],
                'step'  : 0.5,
                'unit'  : u'°C',
                'title' : gettext('Temperature difference (ON)'),
                'desc'  : u'Ustaw wartość różnicy temperatur powodującą załączenie układu solarnego' },
               {'name'  : "solar_off",
                'value' : 8,
                'range' : [0.5,15],
                'step'  : 0.5,
                'unit'  : u'°C',
                'title' : gettext('Temperature difference (OFF)'),
                'desc'  : u'Ustaw wartość różnicy temperatur powodującą wyłączenie układu solarnego' }]

    return render_template("data_rows.html",
                           active='solar',
                           data=values,
                           title=title)

@app.route('/set-room-temp', methods=['GET', 'POST'])
@app.route('/options/change-<name>', methods=['GET', 'POST'])
@app.route('/heater/change-<name>', methods=['GET', 'POST'])
@app.route('/solar/change-<name>', methods=['GET', 'POST'])
@app.route('/water/change-<name>', methods=['GET', 'POST'])
@app.route('/circulation/change-<name>', methods=['GET', 'POST'])
def set_value(name=None):
    # get those data from SQL(name):
    slider = {'min'   : 10,
              'max'   : 80,
              'value' : 17,
              'step'  : 0.1,
              'unit'  : u'°C'}
    description = {'title'  : gettext('Example modal'),
                   'info'   : gettext('Move it'),
                   's_info' : gettext('Temperature')+':'}

    form = RangeForm()
    form.slider.validate(form,[NumberRange(slider['min'],slider['max'])])

    if form.validate_on_submit():
        val = request.form['slider']
        print(val)
        if name is None:
            return redirect('/')

        print(name)
        return redirect('/' + request.path.split('/')[1])

    return render_template("forms/modal-range.html",action=request.path,slider=slider,desc=description,form=form)

@app.route('/options', methods=['GET', 'POST'])
def options():
    options = OptionsForm()
    options.apparent.description = apparent()
    if options.validate_on_submit():
        if options.data['apparent'] is not None:
            options.apparent.description = apparent(True)
        if options.data['reboot']:
            reboot()
        if options.data['reboot_mcu']:
            reboot_mcu()

    hyst_val = 0.5
    return render_template("content/options.html",
                           active='options',
                           options = options,
                           hysteresis_value=hyst_val)