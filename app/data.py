from .models import *
from app import db
from config import DESCRIPTIONS

def get_query(db_model):
    try:
        q = db.session.query(db_model).order_by(db_model.id.desc()).first()
    except AttributeError:
        try:
            q = db.session.query(db_model).order_by(db_model.topic.desc()).first()
        except AttributeError:
            return None
    return q

def get_SQL_last_row(db_model=IndexMqtt):
    q = get_query(db_model)
    d = {}
    for col in q.__table__.columns._data.keys():
        d[col] = getattr(q,col)
    return d

def get_SQL_value(db_model=IndexMqtt,column='payload'):
    q = get_query(db_model)
    try:
        return getattr(q,column)
    except AttributeError:
        return None
    except TypeError:
        return None

def change_setting(name,value):
    d = get_SQL_last_row(IndexMqtt)
    if name in d.keys():
        d[name] = value
    del d['index']
    del d['timestamp']
    db.session.add(Settings(**d))
    db.session.commit()

def parse_timetable(input_json):
    out = []

    out.append({'title' : gettext('Week'),
               'id'     : 'week',
               'states' : input_json['week']})
    return out

def populate(order,dataset=None,keys=None):
    if keys is None:
        keys = ['range', 'unit', 'desc', 'step', 'title']
    if type(order) != list:
        order = [order]
    
    category = dataset.keys()[0]
    data = []
    for name in order:
        d = {}
        d['name'] = name
        try:
            d['value'] = dataset[category][name]
        except TypeError:
            pass
        for k in keys:
            try:
                #d[k] = app.config['DESCRIPTIONS'][category][name][k]
                d[k] = DESCRIPTIONS[category][name][k]
            except KeyError:
                pass
        data.append(d)
    return data

def get_data(datatype='sensors',which='all'):
    values = {}
    if (datatype == 'sensors'):
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
            values['state'] = {'burner'       : status[3],
                               'solar_switch' : status[0],
                               'heater_switch': status[2],
                               'solar_pump'   : status[1],
                               'circulation'  : status[4]}
    else:
        if(which == 'circulation' or which == 'all'):
            values['circulation'] = {
                   'interval' : int(get_SQL_value(SolarControlCirculateInterval)),
                   'time_on' : int(get_SQL_value(SolarControlCirculateTimeOn))}
        if(which == 'heater' or which == 'all'):
            values['heater'] = {
                   'critical' : float(get_SQL_value(SolarControlHeaterCritical)),
                   'expected' : float(get_SQL_value(SolarControlHeaterExpected)),
                   'hysteresis' : float(get_SQL_value(SolarControlHeaterHysteresis)),
                   'schedule' : get_SQL_value(SolarControlHeaterScheduleOn)} #FIXME
        if(which == 'solar' or which == 'all'):
            values['solar'] = {
                   'critical' : float(get_SQL_value(SolarControlSolarCritical)),
                   'temp_on' : float(get_SQL_value(SolarControlSolarOn)),
                   'temp_off' : float(get_SQL_value(SolarControlSolarOff))} 
        if(which == 'tank' or which == 'all'):
            values['tank'] = {
                   'heater_max' : float(get_SQL_value(SolarControlTankHeaterMax)),
                   'heater_min' : float(get_SQL_value(SolarControlTankHeaterMin)),
                   'solar_max' : float(get_SQL_value(SolarControlTankSolarMax))}
    return values
