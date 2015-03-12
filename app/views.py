# -*- coding: UTF-8 -*-

from flask import render_template, redirect, request
from flask.ext.babel import gettext
from wtforms.validators import NumberRange
from app import app, babel, db
import json

from .forms import *
from config import LANGUAGES
from .system import *
from .data import *


def apparent(toggle=False):
    #get apparent temperature switch state from SQL
    apparent = True

    if toggle:
        apparent = not apparent

    return apparent

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
    data = { "inside_temperature" : 20,
             "apparent_temperature" : 21,
             "humidity"  : 50,
             "outside_temperature"  : 10,
             "work_mode" : gettext('Normal'),
             "heater_status" : gettext('ON'),
             "solar_status"  : gettext('ON') }
    #data = dashboard_data()
    return render_template("content/dashboard.html",
                           active='dashboard',
                           title='',
                           user=user,
                           refresh_rate=get_SQL_value('refresh_rate',Settings),
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

    return render_template("forms/modal-range.html",
                           action=request.path,
                           slider=slider,
                           desc=description,
                           form=form)

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
    return render_template("/content/scheme.html",
                           active='scheme',
                           data=values,
                           title=gettext('Scheme'))

@app.route('/water/')
def water():
    # get setpoints from SQL
    settings = get_SQL_last_row(Settings)

    order = ['tank_solar_max', 'tank_heater_max', 'tank_heater_min']
    data = refresh_data('water')
    data += populate(order,settings)

    return render_template("data_rows.html",
                           active='water',
                           data=data,
                           title=gettext('Water'))

@app.route('/circulation/')
def circulation():
    # get setpoints from SQL
    settings = get_SQL_last_row(Settings)

    order = ['circulation_temp','circulation_hysteresis','circulation_solar',
             'circulation_time_on','circulation_time_off']
    val = populate(order,settings)

    return render_template("data_rows.html",
                           active='circulation',
                           data=val,
                           title=gettext('Circulation'))

@app.route('/heater', methods=['GET', 'POST'])
def heater():
    schedule = json.loads(get_SQL_value('schedule',Settings))
    print(schedule['week'])

    # TODO write form for this:
    values = [{'title' : gettext('Work day'),
               'id'    : 'work_day',
               'table' : {
                   'title'     : gettext('Heating schedule'),
                   'col_names' : [gettext('FROM'),gettext('TO'),u'T [°C]'],
                   'data'      : schedule['work'],
                   'footer'    : [gettext('Other'),gettext('Hours'),schedule['other']]}},
              {'title' : gettext('Free day'),
               'id'    : 'free_day',
               'table' : {
                   'title'     : gettext('Heating schedule'),
                   'col_names' : ['OD','DO',u'T [°C]'],
                   'data'      : schedule['free'],
                   'footer'    : [gettext('Other'),gettext('Hours'),schedule['other']]}},
              {'title'  : gettext('Week'),
               'id'     : 'week',
               'states' : schedule['week']}
               ]

     #Validator (move it to client-side JS)
#    for i in range(len(list_FROM)):
#        if list_TO[i] < list_FROM[i]:
#            print("Error - hour_TO is earlier than hour_FROM")
#            break
#        for j in range(len(list_FROM)-i):
#            if list_FROM[j] < list_FROM[i] < list_TO[j]:
#                print("Error - conflicting ranges")
#            if list_FROM[j] < list_TO[i] < list_TO[j]:
#                print("Error - conflicting ranges")
    week = WeekForm()
    init_tab = 1
    if week.validate_on_submit():
        i = 0
        for k in sorted(week.data):
            if week.data[k]:
                values[2]['states'][i] = abs(values[2]['states'][i]-1)
            i+=1
        init_tab = 3

    # save to SQL
    #if week.validate_on_submit() or timetable.validate_on_submit():
    if week.validate_on_submit():
        change_setting('schedule',json.dumps(schedule))

    return render_template("content/heater.html",
                           active='heater',
                           tabs=values,
                           save=True,
                           week_form=week,
                           init_tab=init_tab,
                           title=gettext('Heater'))

@app.route('/solar/')
def solar():
    # get setpoints from SQL
    settings = get_SQL_last_row(Settings)
    order = ['solar_critical','tank_solar_max','solar_on','solar_off']
    data = refresh_data('solar')
    data += populate(order,settings)

    return render_template("data_rows.html",
                           active='solar',
                           data=data,
                           title=gettext("Solar"))

@app.route('/get_SQL_value-<name>', methods=['POST'])
def refresh_data(name):
    # get from sensors SQL db
    data = [ {'title' : gettext('Current temperature'), 'value' : 11 }]
    if request.method == "POST":
        print("OK")
    return data

@app.route('/dashboard/get_data', methods=['POST'])
def dashboard_data():
    data = { "inside_temperature" : 30,
             "apparent_temperature" : 31,
             "humidity"  : 90,
             "outside_temperature"  : 20,
             "work_mode" : gettext('Normal'),
             "heater_status" : gettext('OFF'),
             "solar_status"  : gettext('OFF') }
    if request.method == "POST":
        return json.dumps(data)
    return(data)

@app.route('/change-<name>', methods=['GET', 'POST'])
@app.route('/options/change-<name>', methods=['GET', 'POST'])
@app.route('/heater/change-<name>', methods=['GET', 'POST'])
@app.route('/solar/change-<name>', methods=['GET', 'POST'])
@app.route('/water/change-<name>', methods=['GET', 'POST'])
@app.route('/circulation/change-<name>', methods=['GET', 'POST'])
def set_value(name=None):
    # get those data from SQL(name):
    if name is None:
        name = 'schedule_override_temp'

    # get value from SQL
    value = get_SQL_value(name,Settings)

    val = populate(name)[0]
    if 'step' not in val:
        val['step'] = 1
    slider = {'min'   : val['range'][0],
              'max'   : val['range'][1],
              'value' : value,
              'step'  : val['step'],
              'unit'  : val['unit']}

    description = {key:val[key] for key in ['title','desc']}

    form = RangeForm()
    form.slider.validate(form,[NumberRange(slider['min'],slider['max'])])

    if form.validate_on_submit():
        val = request.form['slider']
        # save to SQL
        change_setting(name,val)
        if name is None:
            return redirect('/')

        return redirect('/' + request.path.split('/')[1])

    return render_template("forms/modal-range.html",
                           action=request.path,
                           slider=slider,
                           desc=description,
                           form=form)

@app.route('/options', methods=['GET', 'POST'])
def options():
    options = OptionsForm()

    data = get_SQL_last_row(Settings)
    options.apparent.description = data['use_apparent_temperature']
    refresh = data['refresh_rate']
    hysteresis = data['room_hysteresis']

    if options.validate_on_submit():
        if options.data['apparent'] is not None:
            options.apparent.description = not options.apparent.description
            change_setting('use_apparent_temperature',options.apparent.description)
        if options.data['reboot']:
            reboot()
        if options.data['reboot_mcu']:
            reboot_mcu()

    return render_template("content/options.html",
                           active='options',
                           options = options,
                           refresh_rate = refresh,
                           hysteresis_value = hysteresis)

def populate(order,SQL_data=None,keys=None):
    if keys is None:
        keys = ['range', 'unit', 'desc', 'step', 'title']
    if type(order) != list:
        order = [order]

    data = []
    for name in order:
        d = {}
        d['name'] = name
        try:
            d['value'] = SQL_data[name]
        except TypeError:
            pass
        for k in keys:
            try:
                d[k] = app.config['DESCRIPTIONS'][name][k]
            except KeyError:
                pass
        data.append(d)
    return data