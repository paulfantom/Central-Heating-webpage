# -*- coding: UTF-8 -*-

from app import db
from time import strftime

class Settings(db.Model):
    index = db.Column(db.Integer, primary_key=True, unique=True)
    timestamp = db.Column(db.String(20))
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

    def __init__(self, circulation_time_off=None, circulation_time_on=None,
                 circulation_solar=None, circulation_hysteresis=None,
                 circulation_temp=None, solar_off=None, solar_on=None,
                 solar_critical=None, tank_solar_max=None,
                 tank_heater_max=None, tank_heater_min=None,
                 room_hysteresis=None, schedule=None,
                 schedule_override_temp=None, use_apparent_temperature=None,
                 refresh_rate=None):
        self.timestamp = strftime("%Y-%m-%dT%H:%M:%S")
        # populate all columns
        l = locals()
        for arg in l:
            setattr(self,arg,l[arg])


#class Data(db.Model):
    #index = db.Column(db.Integer, primary_key=True, unique=True)
    #timestamp = db.Column(db.String(20))

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