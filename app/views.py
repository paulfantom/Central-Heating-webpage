from flask import render_template, flash, redirect
from app import app
#from .forms import LoginForm


#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for OpenID="%s", remember_me=%s' %
#              (form.openid.data, str(form.remember_me.data)))
#        return redirect('/dashboard')
#    return render_template('login.html', 
#                           title='Sign In',
#                           form=form,
#                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
@app.route('/dashboard')
def dashboard():
    user = {'nickname': 'Dupa'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("content/dashboard.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/status')
def status():
    return render_template("content/status.html", title='Status')

@app.route('/water')
def water():
    return render_template("content/water.html", title='Water')

@app.route('/heater')
def heater():
    return render_template("content/heater.html", title='Heater')

@app.route('/solar')
def solar():
    return render_template("content/solar.html", title='Solar')

@app.route('/options')
def options():
    return render_template("content/options.html", title='Options')