from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import TextField, SubmitField, DateTimeField, DecimalField,\
                           HiddenField, BooleanField, PasswordField
from wtforms import ValidationError

from wtforms.validators import Optional

from flask.ext.babel import lazy_gettext as _
from app import babel

class NextFormMixin():
    next = HiddenField()

    def validate_next(self, field):
        if field.data and not validate_redirect_url(field.data):
            field.data = ''
            flash(*get_message('INVALID_REDIRECT'))
            raise ValidationError(get_message('INVALID_REDIRECT')[0])


class LoginForm(Form,NextFormMixin):
    username = TextField(_('username'))
    password = PasswordField(_('password'))
    remember = BooleanField(_('remember_me'))
    submit = SubmitField(_('login'))

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


class RowForm(Form):
    time_from   = DateTimeField(format="%H:%M")
    time_to     = DateTimeField(format="%H:%M")
    temperature = DecimalField(places=1,use_locale=True)
