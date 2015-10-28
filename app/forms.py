from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import TextField, SubmitField, DateTimeField, DecimalField,\
                           HiddenField, BooleanField, PasswordField
from wtforms import ValidationError

from wtforms.validators import Optional, EqualTo, Required, Length

from flask import request
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
    username = TextField(_('Username'),validators=[Required()],description=_('Username'))
    password = PasswordField(_('Password'),validators=[Required()],description=_('Password'))
    remember = BooleanField(_('Remember me'))
    submit = SubmitField(_('Login'))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if not self.next.data:
            self.next.data = request.args.get('next', '')
        self.remember.default = False
#        self.remember.default = config_value('DEFAULT_REMEMBER_ME')

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        if self.username.data.strip() == '':
            self.username.errors.append(_("No username provided"))
            return False

        if self.password.data.strip() == '':
            self.password.errors.append(_("No password provided"))
            return False
        
        return True


class RangeForm(Form):
    slider = DecimalRangeField('Slider', validators=[Required()])
    submit = SubmitField(_('Save'))


class PasswordForm(Form):
   password = PasswordField(_('New password'), [
        Required(),
        Length(min=8, message='Password too short. Minimum 8 signs'),
        EqualTo('confirm', message=_('Passwords must match')) ], description=_("New password"))
   confirm = PasswordField(_('Repeat password'), description=_("Repeat password"))
   submit = SubmitField(_('Change'))


class OptionsForm(Form):
    apparent   = SubmitField(_('Use apparent temperature'),
                             validators=[Optional()],
                             description=True)
    reboot     = SubmitField(_('Reboot HMI'),validators=[Optional()])
    reboot_mcu = SubmitField(_('Reboot MCU'),validators=[Optional()])
    reset_pass = SubmitField(_('Reset password'),validators=[Optional()])


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
