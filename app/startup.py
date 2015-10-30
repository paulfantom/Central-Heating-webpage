
from app import app, db, bcrypt
from app.core.models import User
from sqlalchemy.exc import OperationalError
from flask import flash
from flask.ext.babel import gettext

@app.before_first_request
def startup():
    try:
        db.create_all()
        user = User.query.filter(User.username == 'admin').first()
    except OperationalError:
        flash(gettext("Cannot connect to database"))
        return
    if not user:
        flash(gettext("Created user")+" 'admin'")
        user = User(username = 'admin', 
                    password = 'password')
        db.session.add(user)
    db.session.commit()
