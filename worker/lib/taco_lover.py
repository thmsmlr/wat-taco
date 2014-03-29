from lib.config import Config

from twilio.rest import TwilioRestClient

ACCOUNT_SID = Config.get("TWILIO", "ACCOUNT_SID")
AUTH_TOKEN = Config.get("TWILIO", "AUTH_TOKEN")

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def notify_taco_lover(phone_number, msg):
    client.messages.create(
        to=phone_number,
        from_="+14385001046",
        body=msg,
    )
