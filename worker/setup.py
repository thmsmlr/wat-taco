import os
from setuptools import setup

setup(
    name = "Wat-Taco Worker",
    version = "0.0.1",
    author = "Thomas Millar",
    author_email = "millar.thomas@gmail.com",
    description = "A tool to notify you when tacos are being sold on are being sold on campus",
    keywords = "University of Waterloo Taco Notifier Worker",
    url = "http://www.wattaco.com",
    install_requires = [
        'pymongo',
        'twilio',
		'uwaterlooapi',
    ],
)

