# -*- coding: UTF-8 -*-

from pymysql.err import OperationalError as OperationalError
from paho.mqtt.publish import single as mqtt_send
from .models import *
from app import db
from config import SERVER_IP,MQTT_ID,DESCRIPTIONS
from json import loads as json_loads

def get_user(username):
    return User.query.filter_by(username=username).first_or_404()

def pass_change(new_pass):
    user = get_user('admin')
    user.password = new_pass
    db.session.add(user)
    db.session.commit()

def get_query(db_model):
    try:
        q = db.session.query(db_model).order_by(db_model.id.desc()).first()
    except AttributeError:
        try:
            q = db.session.query(db_model).order_by(db_model.topic.desc()).first()
        except AttributeError:
            return None
    return q

#def get_SQL_last_row(db_model=IndexMqtt):
#    q = get_query(db_model)
#    d = {}
#    for col in q.__table__.columns._data.keys():
#        d[col] = getattr(q,col)
#    return d

def get_SQL_value(db_model=Room1TempReal,column='payload'):
    try:
        q = get_query(db_model)
    except Exception:
        return 0
    try:
        return getattr(q,column)
    except AttributeError:
        return None
    except TypeError:
        return None

def change_setting(value,name,category=None):
     solarControlID = 'solarControl'
     #print("<Category %r>" % category)
     #print("<Name %r>" % name)
     #print("<Value %r>" % value)
     uri = solarControlID + '/'
     if category == 'circulation': category = 'circulate'
     if category is not None:
         uri = uri + category + '/'
     if name == 'room':
        uri = 'room/1/use_apparent'
        value = int(value)
     else:
        uri = uri + 'settings/' + name
     print(uri)
     #name = 'solarControl/heater/critical'
     print(value)
     mqtt_send(uri, str(value), hostname=SERVER_IP, client_id=MQTT_ID)


#def change_setting(name,value):
#    d = get_SQL_last_row(IndexMqtt)
#    if name in d.keys():
#        d[name] = value
#    del d['index']
#    del d['timestamp']
#    db.session.add(Settings(**d))
#    db.session.commit()

#{ 'mon' : { 'from' : TIME, 'to' : TIME, 'temp' : FLOAT }, 'tue' : ..... , 'deafult' : FLOAT }
def parse_timetable(input_json):
    out = []

    out.append({'title' : gettext('Week'),
               'id'     : 'week',
               'states' : input_json['week']})
    return out

def get_description(order,dataset=None,keys=None):
    if keys is None:
        keys = ['range', 'unit', 'desc', 'step', 'title']
    if type(order) != list:
        order = [order]
    
    if dataset is not None: 
        try:
            category = dataset.keys()[0]
        except AttributeError:
            category = dataset
    
    data = []
    for name in order:
        d = {}
        d['name'] = name
        try:
            d['value'] = dataset[category][name]
        except TypeError:
            d['value'] = 0
        for k in keys:
            try:
                d[k] = DESCRIPTIONS[category][name][k]
            except KeyError:
                pass
        data.append(d)
    return data

def get_full_data(dataset='sensors',which='all'):
    values = {}
    if (dataset == 'sensors'):
        if (which == 'outside' or which == 'all'):
            values['outside'] = {'real_temp' : round(float(get_SQL_value(OutsideTemp)),1)}
        if (which == 'room' or which == 'all'):
            values['room'] =  {'inside_temperature'   : round(float(get_SQL_value(Room1TempReal)),1),
                               'apparent_temperature' : round(float(get_SQL_value(Room1TempFeel)),1),
                               'humidity'      : round(float(get_SQL_value(Room1Humidity)),1),
                               'pressure'      : int(float(get_SQL_value(Room1Pressure)))}
        if (which == 'solar' or which == 'all'):
            temps = []
            temps.append(round(float(get_SQL_value(SolarControlSolarTempIn)),1))
            temps.append(round(float(get_SQL_value(SolarControlSolarTempOut)),1))
            values['solar'] = {'temp'     : round(float(get_SQL_value(SolarControlSolarTemp)),1),
                               'temp_in'  : temps[0],
                               'temp_out' : temps[1],
                               'temp_diff': temps[0] - temps[1],
                               'flow'     : int(get_SQL_value(SolarControlSolarPump))}
        if (which == 'heater' or which == 'all'):
            temps = []
            temps.append(round(float(get_SQL_value(SolarControlHeaterTempIn)),1))
            temps.append(round(float(get_SQL_value(SolarControlHeaterTempOut)),1))
            values['heater'] = {'temp_in'  : temps[0],
                                'temp_out' : temps[1],
                                'temp_diff': temps[0] - temps[1]}
        if (which == 'tank' or which == 'all'):
            values['tank'] = {'temp_up' : round(float(get_SQL_value(SolarControlTankTempUp)),1)} 
        if (which == 'state' or which == 'all' or which == 'heater' or which == 'solar'):
            actuators = int(get_SQL_value(SolarControlActuators))
            status = []
            for i in range(0,6):
                status.append(actuators&(2**i) != 0)
            print(bin(actuators))
            values['state'] = {'burner'       : status[3],
                               'solar_switch' : status[0],
                               'heater_switch': status[2],
                               'solar_pump'   : status[1],
                               'circulation'  : status[4]}
    else:
        if(which == 'circulation' or which == 'all'):
            values['circulation'] = {
                   'interval' : int(get_SQL_value(SolarControlCirculationSettingsInterval)),
                   'time_on' : int(get_SQL_value(SolarControlCirculationSettingsTimeOn))}
        if(which == 'heater' or which == 'all'):
            values['heater'] = {
                   'critical' : float(get_SQL_value(SolarControlHeaterSettingsCritical)),
                   'expected' : float(get_SQL_value(SolarControlHeaterSettingsExpected)),
                   'hysteresis' : float(get_SQL_value(SolarControlHeaterSettingsHysteresis)),
                   'schedule' : str(get_SQL_value(SolarControlHeaterSettingsSchedule))} #TODO parse to JSON
        if(which == 'solar' or which == 'all'):
            values['solar'] = {
                   'critical' : float(get_SQL_value(SolarControlSolarSettingsCritical)),
                   'temp_on' : float(get_SQL_value(SolarControlSolarSettingsOn)),
                   'temp_off' : float(get_SQL_value(SolarControlSolarSettingsOff))} 
        if(which == 'tank' or which == 'all'):
            values['tank'] = {
                   'heater_max' : float(get_SQL_value(SolarControlTankSettingsHeaterMax)),
                   'heater_min' : float(get_SQL_value(SolarControlTankSettingsHeaterMin)),
                   'solar_max' : float(get_SQL_value(SolarControlTankSettingsSolarMax))}
    return values

#def get_full_data(dataset='sensors',which='all'):
#    values = {}
#    if (dataset == 'sensors'):
#        if (which == 'outside' or which == 'all'):
#            values['outside'] = {}
#            for key in ['real_temp']: values['outside'][key] = round(get_data(key,'outside',dataset),1)
#        if (which == 'room' or which == 'all'):
#            values['room'] =  {'inside_temperature'   : round(float(get_SQL_value(Room1TempReal)),1),
#                               'apparent_temperature' : round(float(get_SQL_value(Room1TempFeel)),1),
#                               'humidity'      : int(float(get_SQL_value(Room1Humidity))),
#                               'pressure'      : int(float(get_SQL_value(Room1Pressure)))}
#        if (which == 'solar' or which == 'all'):
#            temps = []
#            temps.append(round(float(get_SQL_value(SolarControlSolarTempIn)),1))
#            temps.append(round(float(get_SQL_value(SolarControlSolarTempOut)),1))
#            values['solar'] = {'temp'     : round(float(get_SQL_value(SolarControlSolarTemp)),1),
#                               'temp_in'  : temps[0],
#                               'temp_out' : temps[1],
#                               'temp_diff': temps[0] - temps[1],
#                               'flow'     : int(get_SQL_value(SolarControlSolarPump))}
#        if (which == 'heater' or which == 'all'):
#            temps = []
#            temps.append(round(float(get_SQL_value(SolarControlHeaterTempIn)),1))
#            temps.append(round(float(get_SQL_value(SolarControlHeaterTempOut)),1))
#            values['heater'] = {'temp_in'  : temps[0],
#                                'temp_out' : temps[1],
#                                'temp_diff': temps[0] - temps[1]}
#        if (which == 'tank' or which == 'all'):
#            values['tank'] = {'temp_up' : round(float(get_SQL_value(SolarControlTankTempUp)),1)} 
#        if (which == 'state' or which == 'all' or which == 'heater' or which == 'solar'):
#            actuators = int(get_SQL_value(SolarControlActuators))
#            status = []
#            for i in range(0,6):
#                status.append(actuators&(2**i) != 0)
#            values['state'] = {'burner'       : status[3],
#                               'solar_switch' : status[0],
#                               'heater_switch': status[2],
#                               'solar_pump'   : status[1],
#                               'circulation'  : status[4]}
#    else:
#        if(which == 'circulation' or which == 'all'):
#            values['circulation'] = {
#                   'interval' : int(get_SQL_value(SolarControlCirculationInterval)),
#                   'time_on' : int(get_SQL_value(SolarControlCirculationTimeOn))}
#        if(which == 'heater' or which == 'all'):
#            values['heater'] = {
#                   'critical' : float(get_SQL_value(SolarControlHeaterCritical)),
#                   'expected' : float(get_SQL_value(SolarControlHeaterExpected)),
#                   'hysteresis' : float(get_SQL_value(SolarControlHeaterHysteresis)),
#                   'schedule' : get_SQL_value(SolarControlHeaterScheduleOn)} #FIXME
#        if(which == 'solar' or which == 'all'):
#            values['solar'] = {
#                   'critical' : float(get_SQL_value(SolarControlSolarCritical)),
#                   'temp_on' : float(get_SQL_value(SolarControlSolarOn)),
#                   'temp_off' : float(get_SQL_value(SolarControlSolarOff))} 
#        if(which == 'tank' or which == 'all'):
#            values['tank'] = {
#                   'heater_max' : float(get_SQL_value(SolarControlTankHeaterMax)),
#                   'heater_min' : float(get_SQL_value(SolarControlTankHeaterMin)),
#                   'solar_max' : float(get_SQL_value(SolarControlTankSolarMax))}
#    return values

# TODO something cleaner???
def get_data(name,category,dataset='sensors'):
    if dataset == 'sensors':
        if category == 'outside':
            if name == 'real_temp': return float(get_SQL_value(OutsideTemp))
        if category == 'room':
            if name == 'inside_temperature'  : return float(get_SQL_value(Room1TempReal))
            if name == 'apparent_temperature': return float(get_SQL_value(Room1TempFeel))
            if name == 'humidity'            : return float(get_SQL_value(Room1Humidity))
            if name == 'pressure'            : return int(float(get_SQL_value(Room1Pressure)))
        if category == 'solar':
            if name == 'temp': return float(get_SQL_value(SolarControlSolarTemp))
            if name == 'flow': return int(get_SQL_value(SolarControlSolarPump)) 
            temps = []
            temps.append(float(get_SQL_value(SolarControlSolarTempIn)))
            temps.append(float(get_SQL_value(SolarControlSolarTempOut)))
            if name == 'temp_in'  : return temps[0]
            if name == 'temp_out' : return temps[1]
            if name == 'temp_diff': return temps[0] - temps[1]
        if category == 'heater':
            temps = []
            temps.append(float(get_SQL_value(SolarControlHeaterTempIn)))
            temps.append(float(get_SQL_value(SolarControlHeaterTempOut)))
            if name == 'temp_in'  : return temps[0]
            if name == 'temp_out' : return temps[1]
            if name == 'temp_diff': return temps[0] - temps[1]
        if category == 'tank':
            if name == 'temp_up' : return float(get_SQL_value(SolarControlTankTempUp)) 
        if category == 'state':
            actuators = int(get_SQL_value(SolarControlActuators))
            if name == 'burner'       : return (actuators&(2**3) != 0)
            if name == 'solar_switch' : return (actuators&(2**0) != 0)
            if name == 'heater_switch': return (actuators&(2**2) != 0)
            if name == 'solar_pump'   : return (actuators&(2**1) != 0)
            if name == 'circulation'  : return (actuators&(2**4) != 0)
    else:
        if category == 'room':
            if name == 'use_apparent' : return bool(int(get_SQL_value(Room1UseApparent)))
        if category == 'circulation':
            if name == 'interval': return int(get_SQL_value(SolarControlCirculationSettingsInterval))
            if name == 'time_on' : return int(get_SQL_value(SolarControlCirculationSettingsTimeOn))
        if category == 'heater':
            if name == 'critical'  : return float(get_SQL_value(SolarControlHeaterSettingsCritical))
            if name == 'expected'  : return float(get_SQL_value(SolarControlHeaterSettingsExpected))
            if name == 'hysteresis': return float(get_SQL_value(SolarControlHeaterSettingsHysteresis))
            if name == 'schedule'  :
                schedule = get_SQL_value(SolarControlHeaterSettingsSchedule)
                if schedule == 0:
                    return None
                schedule = schedule.replace('\\','').replace('\'','"')
                if schedule[0] == '"':
                    schedule = schedule[1:-1]
                return json_loads(schedule)
        if category == 'solar':
            if name == 'critical': return float(get_SQL_value(SolarControlSolarSettingsCritical))
            if name == 'temp_on' : return float(get_SQL_value(SolarControlSolarSettingsOn))
            if name == 'temp_off': return float(get_SQL_value(SolarControlSolarSettingsOff)) 
        if category == 'tank':
            if name == 'heater_max': return float(get_SQL_value(SolarControlTankSettingsHeaterMax))
            if name == 'heater_min': return float(get_SQL_value(SolarControlTankSettingsHeaterMin))
            if name == 'solar_max' : return float(get_SQL_value(SolarControlTankSettingsSolarMax))
    return None
