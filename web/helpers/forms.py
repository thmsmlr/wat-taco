from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, ValidationError
from helpers.util import parse_phone_number

class PhoneNumberField(TextField):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = parse_phone_number(valuelist[0])
        else:
            self.data = None

class PhoneNumber():
    def __call__(self, form, field):
        if len(field.data) != 10:
            raise ValidationError("Input must be a 10-digit phone number")

class SignupForm(Form):
    phone_number = PhoneNumberField('phone_number', validators = [Required(), PhoneNumber()])

class UnsubscribeForm(Form):
    phone_number = PhoneNumberField('phone_number', validators = [Required(), PhoneNumber()])
