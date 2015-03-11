from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import SubmitField

from wtforms.validators import NumberRange, Optional

from flask.ext.babel import lazy_gettext as _
from app import babel

class RangeForm(Form):
    slider = DecimalRangeField('Slider')
    submit = SubmitField(_('Save'))

class OptionsForm(Form):
    apparent   = SubmitField(_('Use apparent temperature'),
                             validators=[Optional()],
                             description=True)
    reboot     = SubmitField(_('Reboot HMI'),validators=[Optional()])
    reboot_mcu = SubmitField(_('Reboot MCU'),validators=[Optional()])

class WeekForm(Form):
    day_1 = SubmitField(_('Monday'),validators=[Optional()])
    day_2 = SubmitField(_('Tuesday'),validators=[Optional()])
    day_3 = SubmitField(_('Wednesday'),validators=[Optional()])
    day_4 = SubmitField(_('Thursday'),validators=[Optional()])
    day_5 = SubmitField(_('Friday'),validators=[Optional()])
    day_6 = SubmitField(_('Saturday'),validators=[Optional()])
    day_7 = SubmitField(_('Sunday'),validators=[Optional()])
