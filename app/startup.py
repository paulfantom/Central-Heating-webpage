
from app import app, db, bcrypt
from app.core.models import User

@app.before_first_request
def startup():
    db.create_all()
    user = User.query.filter(User.username == 'admin').first()
    if not user:
        print("Creating user")
        user = User(username = 'admin', 
                    password = 'password')
        db.session.add(user)
    db.session.commit()
