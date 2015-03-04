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
                           active='dashboard',
                           title='',
                           user=user,
                           data=data)

@app.route('/status')
def status():
    values = []
    return render_template("/content/status.html",active='status',data=values)

@app.route('/water')
def water():
    values = [ {'title' : u'Aktualna temperatura',
                'value' : 44 },
               {'name'  : "solar_max",
                'value' : 90,
                'range' : [30,100],
                'title' : u'Solar',
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z kolektora' },
               {'name'  : "heater_max",
                'value' : 90,
                'range' : [30,100],
                'title' : u'Piec (max)',
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z pieca' },
               {'name'  : "heater_min",
                'value' : 30,
                'range' : [30,100],
                'title' : u'Piec (min)',
                'desc'  : u'Ustaw minimalną temperaturę wody w zbiorniku dla zasilania z pieca' }]

    return render_template("data_rows.html", control_buttons=[u'Anuluj',u'Zapisz'],
                           active='water',
                           data=values,
                           title='Woda')

@app.route('/circulation')
def circulation():
    values = [ {'name'  : "circulation_temp",
                'value' : 40,
                'range' : [30,100],
                'unit'  : u'°C',
                'title' : u'Temperatura pracy',
                'desc'  : u'Ustaw temperaturę pracy pompy cyrkulacyjnej' },
               {'name'  : "circulation_hyst",
                'value' : 4,
                'range' : [0.5,10],
                'step'  : 0.5,
                'unit'  : u'°C',
                'title' : u'Histereza pracy',
                'desc'  : u'Ustaw histerezę pracy pompy cyrkulacyjnej' },
               {'name'  : "circulation_solar",
                'value' : 70,
                'range' : [30,150],
                'unit'  : u'°C',
                'title' : u'Wymagana temperatura kolektora',
                'desc'  : u'Ustaw minimalną temperaturę kolektora dla załączenia cyrkulacji' },
               {'name'  : "time_on",
                'value' : 30,
                'range' : [1,300],
                'unit'  : 's',
                'title' : u'Czas pracy',
                'desc'  : u'Ustaw czas pracy pompy w trybie poboru wody' },
               {'name'  : "time_off",
                'value' : 30,
                'range' : [1,180],
                'unit'  : ' min',
                'title' : u'Przerwa',
                'desc'  : u'Ustaw przerwę w pracy pompy w trybie poboru wody' } ]
    return render_template("data_rows.html", control_buttons=[u'Anuluj',u'Zapisz'],
                           active='circulation',
                           data=values,
                           title="Cyrkulacja")

@app.route('/heater')
def heater():
    values = [{'title' : u'Doba robocza',
               'id'    : 'work_day',
               'table' : {
                   'title'     : u'Harmonogram pracy pieca',
                   'col_names' : ['OD','DO',u'T [°C]'],
                   'data'      : [['10:00','20:23',21],['23:01','23:59',20]],
                   'footer'    : [u'Pozostałe',u'godziny',18]}},
              {'title' : u'Doba świąteczna',
               'id'    : 'free_day',
               'table' : {
                   'title'     : u'Harmonogram pracy pieca',
                   'col_names' : ['OD','DO',u'T [°C]'],
                   'data'      : [['06:00','12:23',21],['15:01','23:59',20]],
                   'footer'    : [u'Pozostałe',u'godziny',16]}},
              {'title' : u'Tydzień',
               'id'    : 'week',
               'data'  : [
                   {'id' : 'mon', 'name' : u'Poniedziałek', 'state' : False},
                   {'id' : 'tue', 'name' : u'Wtorek', 'state' : False},
                   {'id' : 'wed', 'name' : u'Środa', 'state' : False},
                   {'id' : 'thu', 'name' : u'Czwartek', 'state' : False},
                   {'id' : 'fri', 'name' : u'Piątek', 'state' : False},
                   {'id' : 'sat', 'name' : u'Sobota', 'state' : True},
                   {'id' : 'sun', 'name' : u'Niedziela', 'state' : True} ]}
               ]

    hyst = { 'name'  : 'hysteresis',
             'title' : u'Histereza',
             'desc'  : u'Ustaw histerezę pracy ogrzewania',
             'value' : 0.5,
             'control_buttons' : [u'Anuluj',u'Zapisz'] }

    save = u'Zapisz'
    return render_template("content/heater.html",
                           active='heater',
                           tabs=values,
                           hysteresis=hyst,
                           save=save,
                           title='Piec')

@app.route('/solar')
def solar():
    values = [ {'title' : u'Aktualna temperatura',
                'value' : 10 },
               {'name'  : "solar_critical",
                'value' : 130,
                'range' : [70,200],
                'unit'  : u'°C',
                'title' : u'Temperatura krytyczna',
                'desc'  : u'Ustaw krytyczną temperaturę wyłączenia kolektora' },
               {'name'  : "solar_tank",
                'value' : 90,
                'range' : [0.5,10],
                'step'  : 0.1,
                'unit'  : u'°C',
                'title' : u'Temperatura wody',
                'desc'  : u'Ustaw maksymalną temperaturę wody w zbiorniku dla zasilania z kolektora' },
               {'name'  : "solar_on",
                'value' : 4,
                'range' : [0.5,15],
                'step'  : 0.5,
                'unit'  : u'°C',
                'title' : u'Delta załączenia',
                'desc'  : u'Ustaw wartość różnicy temperatur powodującą załączenie układu solarnego' },
               {'name'  : "solar_off",
                'value' : 8,
                'range' : [0.5,15],
                'step'  : 0.5,
                'unit'  : u'°C',
                'title' : u'Delta wyłączenia',
                'desc'  : u'Ustaw wartość różnicy temperatur powodującą wyłączenie układu solarnego' }]

    return render_template("data_rows.html", control_buttons=[u'Anuluj',u'Zapisz'],
                           active='solar',
                           data=values,
                           title="Solar")

@app.route('/options')
def options():

    buttons = [[{'name'  : 'refresh',
                 'type'  : 'success',
                 'text'  : u'Odśwież'},
                {'name'  : 'refresh_rate',
                 'type'  : 'primary',
                 'text'  : u'Częstotliwość odświeżania:',
                 'value' : '1'}],
               [{'name'  : 'reboot',
                 'type'  : 'danger',
                 'text'  : u'Zresetuj HMI'},
                {'name'  : 'reboot_mcu',
                 'type'  : 'danger',
                 'text'  : u'Zresetuj sterownik'}]]

    return render_template("content/options.html",
                           active='options',
                           data=buttons)