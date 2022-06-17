from twilio.rest import Client
from random import randint
from geopy.geocoders import Nominatim

location = Nominatim(user_agent="atm")
address = location.geocode("Alangulam")

SID = [
    'AC3ec941c780601b0746e7142d91322dc9',
    'AC208b1adfa448702027fe3d965dc92d86',
    'AC7f6bcb433d0c80c8602676daa91b1988',
    'AC100204cedf61f90653375cbdfda7a4ec',
    ]

TOKEN = [
    'ada97108ed6c5ab2677e539905b3de68',
    '5da58f77356d20180121d64bc78e2c96',
    '5ac8a3a43463b2b59a33e36cfe11ef29',
    'c719c95d7ca1222b6347ca1ee55917c3',
    ]

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
