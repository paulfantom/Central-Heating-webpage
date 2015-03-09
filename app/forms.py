from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import SubmitField

from wtforms.validators import NumberRange, Optional

from flask.ext.babel import gettext

class RangeForm(Form):
    slider = DecimalRangeField('Slider')
    submit = SubmitField(gettext('Save'))

class OptionsForm(Form):
    apparent   = SubmitField(gettext('Use apparent temperature'),
                             validators=[Optional()],
                             description=True)
    reboot     = SubmitField(gettext('Reboot HMI'),validators=[Optional()])
    reboot_mcu = SubmitField(gettext('Reboot MCU'),validators=[Optional()])
