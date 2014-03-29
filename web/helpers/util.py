from twilio.rest import TwilioRestClient

import re

NUMBER_REGEX = re.compile(r'[^\d.]+')

def parse_phone_number(number_str):
    return NUMBER_REGEX.sub('', number_str)

def notify_taco_lover(phone_number, config):
    ACCOUNT_SID = config["TWILIO_ACCOUNT_SID"]
    AUTH_TOKEN = config["TWILIO_AUTH_TOKEN"]

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to=phone_number,
        from_="+14385001046",
        body="Congratulations you've officially been subscribed to Wat Taco!",
    )
