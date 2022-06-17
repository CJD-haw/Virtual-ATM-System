from twilio.rest import Client
from random import randint
from geopy.geocoders import Nominatim

location = Nominatim(user_agent="atm")
address = location.geocode("Alangulam")

SID = []

TOKEN = []

SENDER = [
    '+14432412447',
    '+19594009748',
    '+19156215329',
    '+15392243184',
    ]

RECEIVER = ['+919361288897', '+919488084189', '+916382106797', '+919629666551']

def generate_pin(destination):
    receive = '+91' + destination
    msg = 'Some one recently changed the pin at {0}.'.format(address)
    content = msg.format(msg)
    i = RECEIVER.index(receive)
    client = Client(SID[i], TOKEN[i])
    client.messages.create(body=content, from_=SENDER[i], to=receive)

def generate_balance(account, destination, debited, current):
    receive = '+91' + destination
    acc = 'X'*8 + account[-4:]
    msg = 'Rs.{0} is debited from your account {1} and current balance is Rs.{2}.'
    content = msg.format(debited, acc, current)
    i = RECEIVER.index(receive)
    client = Client(SID[i], TOKEN[i])
    client.messages.create(body=content, from_=SENDER[i], to=receive)

def generate_alert(destination):
    receive = '+91' + destination
    msg = 'Some one wrongly entered the pin at {0} '.format(address)
    content = msg.format(destination)
    i = RECEIVER.index(receive)
    client = Client(SID[i], TOKEN[i])
    client.messages.create(body=content, from_=SENDER[i], to=receive)
