# -*- coding: UTF-8 -*-

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
    user='admin'
    data = { "room_temp" : 20,
             "feel_temp" : 21,
             "humidity"  : 60,
             "out_temp"  : 19,
             "work_mode" : 'normal',
             "heater_status" : 'on',
             "solar_status"  : 'on' }
    return render_template("content/dashboard.html",
                           title='Home',
                           user=user,
                           data=data)

@app.route('/status')
def status():
    return render_template("content/status.html", title='Status')

@app.route('/water')
def water():
    names = ['Solar', 'Heater']
    values = { "solar_max"  : 70,
               "heater_max" : 60,
               "heater_min" : 30 }

    values = [ {'title'  : u'Aktualna temp.',
                'value' : 44 },
               {'name'  : ["solar_max"],
                'value' : [90],
                'range' : [30,100],
                'title' : u'Solar',
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z kolektora' },
               {'name'  : ["heater_max","heater_min"],
                'value' : [90,30],
                'range' : [30,100],
                'title' : u'Piec',
                'desc'  : [u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z pieca',
                           u'Ustaw minimalną temperaturę wody w zbiorniku dla zasilania z pieca'] } ]

    return render_template("content/water.html",
                           title='Water',
                           names=names,
                           data=values)

@app.route('/circulation')
def circulation():
    values = [ {'name'  : "circulation_temp",
                'value' : 40,
                'range' : [30,100],
                'unit'  : u'°C',
                'title' : 'Temperatura pracy',
                'desc'  : u'Ustaw temperaturę pracy pompy cyrkulacyjnej' },
               {'name'  : "circulation_hyst",
                'value' : 4,
                'range' : [0.5,10],
                'unit'  : u'°C',
                'title' : 'Histereza pracy',
                'desc'  : u'Ustaw histerezę pracy pompy cyrkulacyjnej' },
               {'name'  : "circulation_solar",
                'value' : 70,
                'range' : [30,150],
                'unit'  : u'°C',
                'title' : 'Wymagana temperatura kolektora',
                'desc'  : u'Ustaw minimalną temperaturę kolektora dla załączenia cyrkulacji' },
               {'name'  : "time_on",
                'value' : 30,
                'range' : [1,300],
                'unit'  : 's',
                'title' : 'Czas pracy',
                'desc'  : u'Ustaw czas pracy pompy w trybie poboru wody' },
               {'name'  : "time_off",
                'value' : 30,
                'range' : [1,180],
                'unit'  : ' min',
                'title' : 'Przerwa',
                'desc'  : u'Ustaw przerwę w pracy pompy w trybie poboru wody' } ]

    return render_template("content/circulation.html",
                           title='Circulation',
                           data=values)

@app.route('/heater')
def heater():
    return render_template("content/heater.html", title='Heater')

@app.route('/solar')
def solar():
    return render_template("content/solar.html", title='Solar')

@app.route('/options')
def options():
    return render_template("content/options.html", title='Options')