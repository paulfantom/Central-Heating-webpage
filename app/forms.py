from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField,IntegerRangeField

from wtforms.validators import NumberRange

class RangeForm(Form):
    scope = [100,150]
    label = u'default_slider'
    slider = IntegerRangeField(id=label,
                               validators=[NumberRange(min=30,
                                                       max=50,
                                                       message='Wrong Value!')])
