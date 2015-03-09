# -*- coding: UTF-8 -*-

from app import db

class Data(db.Model):
    index = db.Column(db.Integer)
    timestamp = db.Column(db.String(), unique=True)