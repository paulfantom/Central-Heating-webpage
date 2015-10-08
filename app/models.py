# coding: utf-8
from app import db

class SolarControlHeaterSchedule(db.Model):
    __tablename__ = 'solarControl_heater_schedule'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)

class IndexMqtt(db.Model):
    __tablename__ = 'index_mqtt'

    topic = db.Column(db.Text, primary_key=True)
    ts = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


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


class Room1Temp2(db.Model):
    __tablename__ = 'room_1_temp_2'

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


class SolarControlActuators(db.Model):
    __tablename__ = 'solarControl_actuators'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlCirculateInterval(db.Model):
    __tablename__ = 'solarControl_circulate_interval'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlCirculatePump(db.Model):
    __tablename__ = 'solarControl_circulate_pump'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlCirculateTimeOn(db.Model):
    __tablename__ = 'solarControl_circulate_time_on'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterCritical(db.Model):
    __tablename__ = 'solarControl_heater_critical'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterExpected(db.Model):
    __tablename__ = 'solarControl_heater_expected'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterHeatingOn(db.Model):
    __tablename__ = 'solarControl_heater_heating_on'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterHysteresis(db.Model):
    __tablename__ = 'solarControl_heater_hysteresis'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterScheduleOff(db.Model):
    __tablename__ = 'solarControl_heater_schedule_off'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlHeaterScheduleOn(db.Model):
    __tablename__ = 'solarControl_heater_schedule_on'

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


class SolarControlSolarCritical(db.Model):
    __tablename__ = 'solarControl_solar_critical'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPidKd(db.Model):
    __tablename__ = 'solarControl_solar_flow_pid_Kd'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPidKi(db.Model):
    __tablename__ = 'solarControl_solar_flow_pid_Ki'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPidKp(db.Model):
    __tablename__ = 'solarControl_solar_flow_pid_Kp'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPwmSMax(db.Model):
    __tablename__ = 'solarControl_solar_flow_pwm_s_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPwmSMin(db.Model):
    __tablename__ = 'solarControl_solar_flow_pwm_s_min'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPwmTMax(db.Model):
    __tablename__ = 'solarControl_solar_flow_pwm_t_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarFlowPwmTMin(db.Model):
    __tablename__ = 'solarControl_solar_flow_pwm_t_min'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarOff(db.Model):
    __tablename__ = 'solarControl_solar_off'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlSolarOn(db.Model):
    __tablename__ = 'solarControl_solar_on'

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


class SolarControlTankHeaterMax(db.Model):
    __tablename__ = 'solarControl_tank_heater_max'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlTankHeaterMin(db.Model):
    __tablename__ = 'solarControl_tank_heater_min'

    id = db.Column(db.Integer, primary_key=True)
    _dtepoch = db.Column(db.String)
    _dtiso = db.Column(db.Text)
    topic = db.Column(db.Text)
    _dthhmm = db.Column(db.Text)
    payload = db.Column(db.Text)
    _dthhmmss = db.Column(db.Text)


class SolarControlTankSolarMax(db.Model):
    __tablename__ = 'solarControl_tank_solar_max'

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
