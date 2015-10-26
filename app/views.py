# -*- coding: UTF-8 -*-

from flask import render_template, redirect, request, g
from flask.ext.babel import gettext
from wtforms.validators import NumberRange
from app import app, babel, db
import json
from datetime import datetime

from .forms import *
from config import LANGUAGES, SERVER_IP, BABEL_DEFAULT_LOCALE, WEEKDAYS
from .system import *
from .data import *

@babel.localeselector
def get_locale():
    #return request.accept_languages.best_match(LANGUAGES.keys())
    return request.accept_languages.best_match(['pl'])

@app.before_request
def before_request():
    #g.user = current_user
    g.user = None 

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
    return render_template("content/dashboard.html",
                           active='dashboard',
                           title='',
                           user=user,
#                           refresh_rate=get_SQL_value(MQTTData('refresh_rate')),
                           refresh_rate=0.5,
                           data=dashboard_data())

#@app.route('/change-schedule_override_temp', methods=['GET', 'POST'])
#@app.route('/set-room-temp', methods=['GET', 'POST'])
#def room_temp():
#    # get those data from SQL(name):
#    slider = {'min'   : 17,
#              'max'   : 28,
#              'value' : round(float(get_SQL_value(SolarControlHeaterSettingsExpected)),1),
#              'step'  : 0.1,
#              'unit'  : u'°C'}
#    description = {'title'  : gettext('Example modal'),
#                   'info'   : gettext('move it'),
#                   's_info' : gettext('Temperature') + ':',
#                   'cancel' : gettext('Cancel'),
#                   'submit' : gettext('Save')}
#
#    form = RangeForm()
#    from wtforms.validators import NumberRange
#    form.slider.validate(form,[NumberRange(slider['min'],slider['max'])])
#
#    if form.validate_on_submit():
#        val = request.form['slider']
#        print(val)
#        return redirect('/')
#
#    return render_template("forms/modal-range.html",
#                           action=request.path,
#                           slider=slider,
#                           desc=description,
#                           form=form)

@app.route('/status')
def status():
    sensors = get_full_data('sensors','all')
    data = {'sensors' : [
              {'title'  : gettext('Outside temperature'), 'name' : 'outside_temp',
               'unit'   : u'°C', 'value' : sensors['outside']['real_temp']},
              {'title'  : gettext('Inside temperature'), 'name' : 'inside_temperature',
               'unit'   : u'°C', 'value' : sensors['room']['inside_temperature'] },
              {'title'  : gettext('Apparent temperature'), 'name' : 'apparent_temperature',
               'unit'   : u'°C', 'value' : sensors['room']['apparent_temperature'] },
              {'title'  : gettext('Humidity'), 'name' : 'humidity',
               'unit'   : u'%',  'value' : sensors['room']['humidity'] },
              {'title'  : gettext('Pressure'), 'name' : 'pressure',
               'unit'   : u'hPa', 'value' : sensors['room']['pressure'] },
              {'title'  : gettext('Solar temperature'), 'name' : 'solar_temp',
               'unit'   : u'°C', 'value' : sensors['solar']['temp']},
              {'title'  : gettext('Solar input'), 'name' : 'solar_in',
               'unit'   : u'°C', 'value' : sensors['solar']['temp_in'] },
              {'title'  : gettext('Solar output'), 'name' : 'solar_out',
               'unit'   : u'°C', 'value' : sensors['solar']['temp_out'] },
              {'title'  : gettext('Solar difference'), 'name' : 'solar_diff',
               'unit'   : u'°C', 'value' : sensors['solar']['temp_diff'] },
              {'title'  : gettext('Tank'), 'name' : 'tank_up',
               'unit'   : u'°C', 'value' : sensors['tank']['temp_up']  },
              {'title'  : gettext('Heater input'), 'name' : 'heater_in',
               'unit'   : u'°C', 'value' : sensors['heater']['temp_in'] },
              {'title'  : gettext('Heater output'), 'name' : 'heater_out',
               'unit'   : u'°C', 'value' : sensors['heater']['temp_out'] },
              {'title'  : gettext('Heater diffrence'), 'name' : 'heater_diff',
               'unit'   : u'°C', 'value' : sensors['heater']['temp_diff'] }],
          'states'  : [
              {'title' : gettext('Burner'), 'name' : 'burner',
               'value' : gettext('ON') if sensors['state']['burner'] else gettext('OFF') },
              {'title' : gettext('DHW/CH actuator'), 'name' : 'heater_switch',
               'value' : gettext('DHW') if sensors['state']['heater_switch'] else gettext('CH') },
              {'title' : gettext('Solar pump'), 'name' : 'solar_pump',
               'value' : gettext('ON') if sensors['state']['solar_pump'] else gettext('OFF') },
              {'title' : gettext('Solar system actuator'), 'name' : 'solar_switch',
               'value' : gettext('ON') if sensors['state']['solar_switch'] else gettext('OFF') },
              {'title' : gettext('Solar circuit flow'), 'name' : 'solar_flow',
               'value' : sensors['solar']['flow'] },
              {'title' : gettext('Circulation'), 'name' : 'circulation',
               'value' : gettext('ON') if sensors['state']['circulation'] else gettext(gettext('OFF')) } ]
              }
    title=gettext('Sensors data')
    return render_template("/content/status.html",
                           active='status',
                           data=data,
                           title=title)

#@app.route('/scheme')
#def scheme():
#    return render_template("/content/scheme.html",
#                           active='scheme',
#                           data=get_full_data('sensors','all'),
#                           title=gettext('Scheme'))

@app.route('/heater/')
@app.route('/tank/')
@app.route('/solar/')
@app.route('/circulation/')
def data_rows():
    uri = request.base_url.replace(request.url_root,'').replace('/','')
    data = []
    if uri == 'circulation':
        order = ['time_on', 'interval']
        title = gettext('Circulation')
    elif uri == 'solar':
        order = ['critical','temp_on','temp_off']
        data  = refresh_data('solar','temp')
        title = gettext('Solar')
    elif uri == 'tank':
        order = ['solar_max', 'heater_max', 'heater_min']
        data  = refresh_data('tank','temp_up')
        title = gettext('Water')
    elif uri == 'heater':
        order = ['expected', 'critical', 'hysteresis']
        title = gettext('Heater')
    
    data += get_description(order,get_full_data('settings',uri))
    return render_template("data_rows.html",
                           active=uri,
                           data=data,
                           refresh_rate=0.5,
                           #refresh_rate=settings['refresh_rate'],
                           title=title)

@app.route('/schedule/change', methods=['POST'])
def schedule_validate():
    print("----SCHEDULE RECEIVED---")
    data = request.get_json(force=True)
    #TODO exceptions
    print(data)
    try:
        data['other'] = round(float(data['other']),2)
        for i in range(7):
            data['week'][i] = int(bool(int(data['week'][i])))
        for day in ('work','free'):
            for i in range(len(data[day])):
                for when in ('from', 'to'):
                    time = data[day][i][when].split(":")
                    data[day][i][when] = []
                    for j in (0,1):
                        data[day][i][when].append(int(time[j]))
                data[day][i]['temp'] = round(float(data[day][i]['temp']),2)
    except (KeyError,IndexError):
        pass
        #return schedule(error=True)
    
    change_setting('"'+json.dumps(data,separators=(',', ':'))+'"','schedule','heater')
    print("--NEW SCHEDULE POSTED--")
    #return schedule()

@app.route('/schedule', methods=['GET','POST'])
def schedule():
    save = True
    schedule = get_data('schedule','heater','settings')
    if schedule is None:
        save=False
        schedule = {"week":[0,0,0,0,0,0,0],
                    "work":[{"to":[0,0],"from":[0,0],"temp":0}],
                    "free":[{"to":[0,0],"from":[0,0],"temp":0}],
                    "other":0}
 
    try:
        diff = datetime.now() - datetime(*schedule['override']['start'])
        duration =  schedule['override']['duration']
        if diff.seconds < duration * 60:
            override_temp = schedule['override']['temp']
        else:
            override_temp = None
    except KeyError:
        override_temp = None
 
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
               'states' : schedule['week'],
               'days'   : WEEKDAYS}
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

    return render_template("content/schedule_new.html",
                           active='schedule',
                           tabs=values,
                           save=save,
                           init_tab=1,
                           override=override_temp,
                           title=gettext('Heater'))

@app.route('/schedule_old', methods=['GET','POST'])
def schedule_old():
    schedule = get_data('schedule','heater','settings')
    #schedule = schedule.replace('\\','').replace('\'','"')
    #schedule = json.loads(schedule)
    #schedule = json.loads(schedule.replace('\\','').replace('\'','"'))

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
    print(week.data)
    if week.validate_on_submit():
        i = 0
        v = []
        for k in sorted(week.data):
            v.append(week.data[k])
            if week.data[k]:
                values[2]['states'][i] = abs(values[2]['states'][i]-1)
            i+=1
        print(v)
        init_tab = 3

    # save to SQL
    #if week.validate_on_submit() or timetable.validate_on_submit():
    if week.validate_on_submit():
        pass
        #print(schedule)
        #change_setting('schedule',json.dumps(schedule))

    return render_template("content/schedule_old.html",
                           active='schedule',
                           tabs=values,
                           save=True,
                           week_form=week,
                           init_tab=init_tab,
                           title=gettext('Heater'))

#@app.route('/get_value_<category>_<subcategory>_<name>', methods=['POST'])
@app.route('/get/<category>/<subcategory>_<name>', methods=['POST'])
@app.route('/get/<category>/<subcategory>/<name>', methods=['POST'])
def refresh_data(subcategory,name,category='sensors'):
    #failsafe
    if '_' in subcategory:
        t = subcategory.split('_')
        subcategory = t[0]
        for i in t[1:]:
            name = i + '_' + name
    data = {'title' : gettext('Current temperature'), 
            'value' : round(get_data(name,subcategory,category),1), 
            'name' : subcategory+'_'+name }
    if request.method == "POST":
        return json.dumps(data)
    return([data])

@app.route('/dashboard/get_data', methods=['POST'])
def dashboard_data():
    day = datetime.today().weekday()
    try: 
        schedule_day = bool(int(get_data('schedule','heater','settings')['week'][day]))
    except TypeError:
        schedule_day = False
    data = { "inside_temperature"   : round(get_data('inside_temperature','room'),1),
             "apparent_temperature" : round(get_data('apparent_temperature','room'),1),
             "use_apparent" : get_data('use_apparent','room','settings'),
             "humidity"  : int(get_data('humidity','room')),
             "pressure"  : int(get_data('pressure','room')),
             "outside_temperature"  : round(get_data('real_temp','outside'),1),
             "tank_temp_up" : round(get_data('temp_up','tank'),1),
             "heater_schedule" : gettext('Free') if schedule_day else gettext('Normal'),
             "heater_status" : gettext('ON') if get_data('burner','state') else gettext('OFF')}
    if request.method == "POST":
        return json.dumps(data)
    return(data)

@app.route('/change-<name>', methods=['GET', 'POST'])
@app.route('/<category>/change-<name>', methods=['GET', 'POST'])
#@app.route('/options/change-<name>', methods=['GET', 'POST'])
#@app.route('/heater/change-<name>', methods=['GET', 'POST'])
#@app.route('/solar/change-<name>', methods=['GET', 'POST'])
#@app.route('/tank/change-<name>', methods=['GET', 'POST'])
#@app.route('/circulation/change-<name>', methods=['GET', 'POST'])
def set_value(name,category=None):
    if name.startswith('schedule'):
       category = 'heater'
       name = 'expected'
    elif '_' in name:
        t = name.split('_')
        subcategory = t[0]
        for i in t[2:]:
            name = i + '_' + name
   
    print(name)
    #val = get_description(order,get_data('settings',uri))
    val = get_description(name,category)[0]
    #if name == 'override_temp':
    #    val['value'] = get_data('expected','heater','settings')
    #else:
    #    val['value'] = get_data(name,category,'settings')
    val['value'] = get_data(name,category,'settings')
    
    #val = get_description(name)[0]
    if 'step' not in val:
        val['step'] = 1
    slider = {'min'   : val['range'][0],
              'max'   : val['range'][1],
              'value' : val['value'],
              'step'  : val['step'],
              'unit'  : val['unit']}

    description = {key:val[key] for key in ['title','desc']}
    
    form = RangeForm()
    form.slider.validate(form,[NumberRange(slider['min'],slider['max'])])

    if form.validate_on_submit():
        val = request.form['slider']
        #save to SQL
        if name == 'expected' and category == 'heater':
            #FIXME insert new into schedule
            schedule = get_data('schedule','heater','settings')
            time = list(datetime.today().timetuple())[0:6]
            schedule['override'] = {'temp' : float(val), 'start' : time, 'duration': 60}
            s = '"' + json.dumps(schedule) + '"'
            change_setting(s,'schedule','heater')
        else:
            change_setting(val,name,category)
        if name is None:
            return redirect('/')
        
        return redirect('/' + request.path.split('/')[-2])

    return render_template("forms/modal-range.html",
                           action=request.path,
                           slider=slider,
                           desc=description,
                           form=form)

@app.route('/options', methods=['GET', 'POST'])
def options():
    #data = get_SQL_last_row(Settings)
    data = {}
    data['use_apparent'] = get_data('use_apparent','room','settings')
    #refresh = data['refresh_rate']
    refresh = 0.5
    #hysteresis = data['room_hysteresis']
    hysteresis = get_data('hysteresis','heater','settings')
    #hysteresis = float(get_SQL_value(SolarControlHeaterSettingsHysteresis))
    
    if request.remote_addr != SERVER_IP:
        print(request.remote_addr)
        print(SERVER_IP)
        return render_template("content/options.html",
                               active='options',
                               options = None,
                               refresh_rate = refresh,
                               hysteresis_value = hysteresis)
    options = OptionsForm()
    options.apparent.description = data['use_apparent_temperature']

    if options.validate_on_submit():
        if options.data['use_apparent'] is not None:
            options.apparent.description = not options.apparent.description
            change_setting('room',options.apparent.description)
        if options.data['reboot']:
            reboot()
        if options.data['reboot_mcu']:
            reboot_mcu()
    
    return render_template("content/options.html",
                           active='options',
                           options = options,
                           refresh_rate = refresh,
                           hysteresis_value = hysteresis)
