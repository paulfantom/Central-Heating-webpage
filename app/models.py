# coding: utf-8
from app import db
#from flask.ext.login import UserMixin
from flask.ext.user import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    is_enabled = True
    active = True
    
    def is_active(self):
        return self.is_enabled


#class UserNotFoundError(Exception):
#    pass
#
#class User(UserMixin):
#     #TODO hash function
#     #TODO save it to file/db
#     USERS = {'admin' : 'password'}     
#
#     def __init__(self, id):
#         if not id in self.USERS:
#             raise UserNotFoundError()
#         self.id = id
#         #TODO read password
#         self.password = self.USERS[id]
#     
#     @classmethod
#     def get(self_class, id):
#         '''Return user instance of id, return None if not exist'''
#         try:
#             return self_class(id)
#         except UserNotFoundError:
#             return None


class SolarControlHeaterSettingsSchedule(db.Model):
    __tablename__ = 'solarControl_heater_settings_schedule'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)

#class IndexMqtt(db.Model):
#    __tablename__ = 'index_mqtt'
#
#    topic = db.Column(db.Text, primary_key=True)
#    ts = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class OutsideTemp(db.Model):
    __tablename__ = 'outside_temp'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class Room1Humidity(db.Model):
    __tablename__ = 'room_1_humidity'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class Room1Pressure(db.Model):
    __tablename__ = 'room_1_pressure'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class Room1TempReal(db.Model):
    __tablename__ = 'room_1_temp_real'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class Room1TempFeel(db.Model):
    __tablename__ = 'room_1_temp_feel'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class Room1UseApparent(db.Model):
    __tablename__ = 'room_1_use_apparent'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlActuators(db.Model):
    __tablename__ = 'solarControl_actuators'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlCirculationSettingsInterval(db.Model):
    __tablename__ = 'solarControl_circulate_settings_interval'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlCirculationPump(db.Model):
    __tablename__ = 'solarControl_circulate_pump'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlCirculationSettingsTimeOn(db.Model):
    __tablename__ = 'solarControl_circulate_settings_time_on'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterSettingsCritical(db.Model):
    __tablename__ = 'solarControl_heater_settings_critical'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterSettingsExpected(db.Model):
    __tablename__ = 'solarControl_heater_settings_expected'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterSettingsHeatingOn(db.Model):
    __tablename__ = 'solarControl_heater_settings_heating_on'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterSettingsHysteresis(db.Model):
    __tablename__ = 'solarControl_heater_settings_hysteresis'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterSettingsScheduleOff(db.Model):
    __tablename__ = 'solarControl_heater_settings_schedule_off'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterSettingsScheduleOn(db.Model):
    __tablename__ = 'solarControl_heater_settings_schedule_on'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterTempIn(db.Model):
    __tablename__ = 'solarControl_heater_temp_in'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterTempOut(db.Model):
    __tablename__ = 'solarControl_heater_temp_out'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsCritical(db.Model):
    __tablename__ = 'solarControl_solar_settings_critical'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsFlowPwmSMax(db.Model):
    __tablename__ = 'solarControl_solar_settings_flow_pwm_s_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsFlowPwmSMin(db.Model):
    __tablename__ = 'solarControl_solar_settings_flow_pwm_s_min'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsFlowPwmTMax(db.Model):
    __tablename__ = 'solarControl_solar_settings_flow_pwm_t_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsFlowPwmTMin(db.Model):
    __tablename__ = 'solarControl_solar_settings_flow_pwm_t_min'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsOff(db.Model):
    __tablename__ = 'solarControl_solar_settings_off'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarSettingsOn(db.Model):
    __tablename__ = 'solarControl_solar_settings_on'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarPump(db.Model):
    __tablename__ = 'solarControl_solar_pump'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarTemp(db.Model):
    __tablename__ = 'solarControl_solar_temp'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarTempIn(db.Model):
    __tablename__ = 'solarControl_solar_temp_in'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarTempOut(db.Model):
    __tablename__ = 'solarControl_solar_temp_out'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlTankSettingsHeaterMax(db.Model):
    __tablename__ = 'solarControl_tank_settings_heater_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlTankSettingsHeaterMin(db.Model):
    __tablename__ = 'solarControl_tank_settings_heater_min'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlTankSettingsSolarMax(db.Model):
    __tablename__ = 'solarControl_tank_settings_solar_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlTankTempUp(db.Model):
    __tablename__ = 'solarControl_tank_temp_up'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)
