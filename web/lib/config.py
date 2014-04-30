from flask import current_app

def get_setting(key):
    return current_app.config[key]

def get_twilio_account_sid():
    return get_setting("TWILIO_ACCOUNT_SID")

def get_twilio_auth_token():
    return get_setting("TWILIO_AUTH_TOKEN")

