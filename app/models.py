# -*- coding: UTF-8 -*-

from app import db
from time import strftime

class Settings(db.Model):
    index = db.Column(db.Integer, primary_key=True, unique=True)
    timestamp = db.Column(db.String(20), unique=True)
    # CIRCULATION
    circulation_time_off = db.Column(db.Integer)
    circulation_time_on = db.Column(db.Float(1))
    circulation_solar = db.Column(db.Integer)
    circulation_hysteresis = db.Column(db.Float(1))
    circulation_temp = db.Column(db.Integer)
    # SOLAR
    solar_off = db.Column(db.Float(1))
    solar_on = db.Column(db.Float(1))
    solar_critical = db.Column(db.Integer)
    # TANK
    tank_solar_max = db.Column(db.Float(1))
    tank_heater_max = db.Column(db.Float(1))
    tank_heater_min = db.Column(db.Float(1))
    # ROOM TEMPERATURE
    room_hysteresis = db.Column(db.Float(1))
    schedule = db.Column(db.Text)
    schedule_override_temp = db.Column(db.Float(1))
    use_apparent_temperature = db.Column(db.Boolean)
    # OTHER
    refresh_rate = db.Column(db.Float(1))

    def __repr__(self):
        return '<Index %r>' % self.index

    def __init__(self, circulation_time_off, circulation_time_on,
                 circulation_solar, circulation_hysteresis, circulation_temp,
                 solar_off, solar_on, solar_critical,
                 tank_solar_max, tank_heater_max, tank_heater_min,
                 room_hysteresis, schedule, schedule_override_temp,
                 use_apparent_temperature, refresh_rate):
        self.timestamp = strftime("%Y-%m-%dT%H:%M:%S")
        self.circulation_time_off = circulation_time_off
        self.circulation_time_on = circulation_time_on
        self.circulation_solar = circulation_solar
        self.circulation_hysteresis = circulation_hysteresis
        self.circulation_temp = circulation_temp
        self.solar_off = solar_off
        self.solar_on = solar_on
        self.solar_critical = solar_critical
        self.tank_solar_max = tank_solar_max
        self.tank_heater_max = tank_heater_max
        self.tank_heater_min = tank_heater_min
        self.room_hysteresis = room_hysteresis
        self.schedule = schedule
        self.schedule_override_temp = schedule_override_temp
        self.use_apparent_temperature = use_apparent_temperature
        self.refresh_rate = refresh_rate

def get_query(db_model):
    try:
        q = db.session.query(db_model).order_by(db_model.index.desc()).first()
    except AttributeError:
        try:
            q = db.session.query(db_model).order_by(db_model.index.desc()).first()
        except AttributeError:
            return None
    return q

def get_last_row(db_model):
    q = get_query(db_model)
    d = {}
    for col in q.__table__.columns._data.keys():
        d[col] = getattr(q,col)
    return d

def get_value(column,db_model=Settings):
    q = get_query(db_model)
    try:
        return getattr(q,column)
    except AttributeError:
        return None
    except TypeError:
        return None

#class Data(db.Model):
    #index = db.Column(db.Integer, primary_key=True, unique=True)
    #timestamp = db.Column(db.String(20), unique=True)

    #solar_temperature = db.Column(db.Float(1))
    #outside_temperature = db.Column(db.Float(1))
    #inside_temperature = db.Column(db.Float(1))
    #apparent_temperature = db.Column(db.Float(1))
    ## STATES
    #burner_state = db.Column(db.Boolean)
    #heater_pump_state = db.Column(db.Boolean)
    #solar_pump_state = db.Column(db.Boolean)
    #circulation_pump_state = db.Column(db.Boolean)
    #solar_system_valve = db.Column(db.Boolean)
    #heater_system_valve = db.Column(db.Boolean)
    ## SOLAR METER
    #solar_temperature_in   = db.Column(db.Float(2))
    #solar_temperature_out  = db.Column(db.Float(2))
    #solar_temperature_diff = db.Column(db.Float(2))
    #solar_flow             = db.Column(db.Integer)
    #solar_energy           = db.Column(db.Integer)
    #solar_volume           = db.Column(db.Float(2))
    #solar_consumption      = db.Column(db.Float(1))
    ## HEATER METER
    #heater_temperature_in   = db.Column(db.Float(2))
    #heater_temperature_out  = db.Column(db.Float(2))
    #heater_temperature_diff = db.Column(db.Float(2))
    #heater_flow             = db.Column(db.Integer)
    #heater_energy           = db.Column(db.Integer)
    #heater_volume           = db.Column(db.Float(2))
    #heater_consumption      = db.Column(db.Float(1))
    ## TANK METER
    #tank_temperature_in   = db.Column(db.Float(2))
    #tank_temperature_out  = db.Column(db.Float(2))
    #tank_temperature_diff = db.Column(db.Float(2))
    #tank_flow             = db.Column(db.Integer)
    #tank_energy           = db.Column(db.Integer)
    #tank_volume           = db.Column(db.Float(2))
    #tank_consumption      = db.Column(db.Float(1))