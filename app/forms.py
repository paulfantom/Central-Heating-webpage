from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import SubmitField

from wtforms.validators import NumberRange, Optional

class RangeForm(Form):
    slider = DecimalRangeField('Slider')
    submit = SubmitField('Submit')

class OptionsForm(Form):
    apparent   = SubmitField('Use apparent temperature',
                             validators=[Optional()],
                             description=True)
    reboot     = SubmitField('Reboot HMI',validators=[Optional()])
    reboot_mcu = SubmitField('Reboot MCU',validators=[Optional()])
