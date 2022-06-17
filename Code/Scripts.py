from tkinter import Tk
from threading import Thread
from tkinter.messagebox import askokcancel
from Backend import *
from Message import *
from Greeting import Greet
from VerifyAccount import Account
from VerifyPIN import Pin
from Menu import Home
from ChangePIN import ChangePinNumber
from ConfirmPIN import ConfirmPinNumber
from Withdrawal import Debit
from Balance import (BBalance, DBalance)
from Smart import trackHand

def alert():
      if askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

def welcoming():
      global ACCOUNT, PIN, BALANCE, PHONE
      ACCOUNT = ''
      PIN = ''
      BALANCE = ''
      PHONE = ''
      welcome = Greet(root, 'intro')
      welcome.show()
      return enteringAccount()

def enteringAccount():
      acc = Account(root)
      option, account = acc.show()
      if account != '':
            global ACCOUNT, PIN, BALANCE, PHONE
            ACCOUNT = account
            PIN = get_pin(account)
            BALANCE = get_balance(account)
            PHONE = get_phone(account)
      if option == 'confirm from account': return enteringPin()
      elif option == 'exit from account': return thanking()
      elif option == 'invalid from account': return welcoming()

def enteringPin():
      global PIN, PHONE
      pin = Pin(root, PIN)
      option = pin.show()
      if option == 'confirm from pin': homing()
      elif option == 'exit from pin': thanking()
      else:
            generate_alert(PHONE)      
      if option == 'invalid from pin': enteringPin()
      elif option == 'wrong from pin': return welcoming()
      
def homing():
      home = Home(root)
      option = home.show()
      if option == 'change pin from home': return changingPin()
      elif option == 'debit from home': return debitAmount()
      elif option == 'balance from home': return balanceAmount()
      elif option == 'exit from home': return thanking()

def changingPin():
      pin = ChangePinNumber(root)
      option, cpin = pin.show()
      if option == 'confirm from change pin': return confirmingPin(cpin)
      elif option == 'home from change pin': return homing()
      elif option == 'invalid from change pin': return changingPin()
      elif option == 'wrong from change pin': return thanking()

def confirmingPin(cpin):
      global ACCOUNT, PIN, PHONE
      pin = ConfirmPinNumber(root, cpin)
      option, CPIN = pin.show()
      if CPIN:
            set_pin(ACCOUNT, CPIN)
            PIN = get_pin(ACCOUNT)
            generate_pin(PHONE)
      if option == 'confirm from confirm pin': return welcoming()
      elif option == 'home from confirm pin': return homing()
      elif option == 'invalid from confirm pin': return confirmingPin(cpin)
      elif option == 'wrong from confirm pin': return thanking()

def debitAmount():
      global ACCOUNT, BALANCE, PIN, PHONE
      debit = Debit(root, BALANCE)
      option, AMT, bal = debit.show()
      if AMT:
            set_balance(ACCOUNT, bal)
            BALANCE = get_balance(ACCOUNT)
            generate_balance(ACCOUNT, PHONE, AMT, BALANCE)
      if option == 'confirm from debit': return balanceDebit(AMT)
      elif option == 'home from debit': return homing()
      elif option == 'insufficient balance': return debitAmount()

def balanceDebit(AMT):
      global BALANCE
      balance = DBalance(root, AMT, BALANCE)
      option = balance.show()
      if option == 'home from dbalance': return homing()
      elif option == 'exit from dbalance': return thanking()

def balanceAmount():
      global BALANCE
      balance = BBalance(root, BALANCE)
      option = balance.show()
      if option == 'home from bbalance': return homing()
      elif option == 'exit from bbalance': return thanking()

def thanking():
      thankyou = Greet(root, 'con')
      thankyou.show()
      return welcoming()

root = Tk()
root.title("Virtual ATM")
root.geometry("1366x768")
root.resizable(0, 0)
root.configure(bg="#5571ff")
root.protocol("WM_DELETE_WINDOW", alert)

rt = Thread(target=welcoming, daemon=True)
rt.start()

rth = Thread(target=trackHand, daemon=True)
rth.start()

root.mainloop()
