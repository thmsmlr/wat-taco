from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, ValidationError
from helpers.util import parse_phone_number

class SignupForm(Form):
    phone_number = TextField('phone_number', validators = [Required()])

    def validate_phone_number(form, field):
        number = parse_phone_number(field.data)

        if len(number) != 10:
            raise ValidationError("Input must be a 10-digit phone number")

class UnsubscribeForm(Form):
    phone_number = TextField('phone_number', validators = [Required()])

    def validate_phone_number(form, field):
        number = parse_phone_number(field.data)

        if len(number) != 10:
            raise ValidationError("Input must be a 10-digit phone number")

