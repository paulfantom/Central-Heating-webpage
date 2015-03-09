# -*- coding: UTF-8 -*-

from app import db

class Settings(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String())
    circulation_time_off = db.Column(db.Integer)
    circulation_time_on = db.Column(db.Real)
    circulation_solar = db.Column(db.Integer)
    circulation_hysteresis = db.Column(db.Real)
    circulation_temp = db.Column(db.Integer)
    solar_off = db.Column(db.Real)
    solar_on = db.Column(db.Real)
    solar_critical = db.Column(db.Integer)
    tank_solar_max = db.Column(db.Real)
    tank_heater_max = db.Column(db.Real)
    tank_heater_min = db.Column(db.Real)
    refresh_rate = db.Column(db.Real)
    apparent_temperature = db.Column(db.Boolean)
    room_hysteresis = db.Column(db.Real)
    #schedule = db.relationship('')

