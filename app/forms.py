from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField

from wtforms.validators import NumberRange

class RangeForm(Form):
    slider = DecimalRangeField(validators=[NumberRange(10,30)])