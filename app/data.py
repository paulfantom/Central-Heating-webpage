from .models import Settings
from app import db

def get_query(db_model):
    try:
        q = db.session.query(db_model).order_by(db_model.index.desc()).first()
    except AttributeError:
        try:
            q = db.session.query(db_model).order_by(db_model.index.desc()).first()
        except AttributeError:
            return None
    return q

def get_last_row(db_model=Settings):
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

def change_setting(name,value):
    d = get_last_row(Settings)
    if name in d.keys():
        d[name] = value
    del d['index']
    del d['timestamp']
    db.session.add(Settings(**d))
    db.session.commit()
