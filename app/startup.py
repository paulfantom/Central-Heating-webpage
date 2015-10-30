
from app import app, db, bcrypt
from app.core.models import User
from sqlalchemy.exc import OperationalError

@app.before_first_request
def startup():
    try:
        db.create_all()
        user = User.query.filter(User.username == 'admin').first()
    except OperationalError:
        return
    if not user:
        print("Creating user")
        user = User(username = 'admin', 
                    password = 'password')
        db.session.add(user)
    db.session.commit()
