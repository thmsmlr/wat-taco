import re

NUMBER_REGEX = re.compile(r'[^\d.]+')

def parse_phone_number(number_str):
    return NUMBER_REGEX.sub('', number_str)

