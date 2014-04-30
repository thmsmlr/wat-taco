from twilio.rest import TwilioRestClient

from lib import config

import re
import random

NUMBER_REGEX = re.compile(r'[^\d.]+')

def parse_phone_number(number_str):
    return NUMBER_REGEX.sub('', number_str)

def notify_taco_lover(phone_number):
    ACCOUNT_SID = config.get_twilio_account_sid()
    AUTH_TOKEN = config.get_twilio_auth_token()

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    # client.messages.create(
    #     to=phone_number,
    #     from_="+14385001046",
    #     body="Congratulations you've officially been subscribed to Wat Taco!",
    # )


TACO_PUNS = [
  "Say hello to my little taco",
  "Do you have what it tacos?",
  "Taco's one to know one",
  "It tacos two to tango",
  "We need to taco",
  "Taco turkey",
  "Taco taco little star",
  "Taco dirty to me",
  "Taco one for the team",
  "Tik-Taco",
  "Hickory Dickory Taco",
  "I'm going to make him a taco he can't refuse",
  "Taco, I've got a feeling we're not in Kansas anymore",
  "Here's looking at you, taco",
  "May the taco be with you",
  "Fasten your seatbelts, it's going to be a bumpy taco",
  "You taco-in' to me?",
  "I love the smell of taco in the morning",
  "I think this is the beginning of a beautiful taco",
  "Show me the taco!",
  "You can't handle the taco!",
  "You're gonna need a bigger taco",
  "There's no place like taco",
  "You had me at taco",
  "A boy's best friend is his taco",
  "Soylent green is tacos!",
  "Hasta la Vista, taco!",
  "I feel the need- the need for tacos!",
  "Nobody puts Baby in a taco",
  "Houston, we have a taco",
  "Tacos? We ain't got no tacos! We don't need no tacos! I don't have to show you any stinking tacos!",
  "We'll always have tacos",
  "I see taco people",
  "Keep your friends close, but your tacos closer"
]

def get_taco_pun():
    return random.choice(TACO_PUNS)

