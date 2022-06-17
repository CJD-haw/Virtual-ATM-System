import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='atm_system')
cursor = db.cursor(buffered=True)

def check_account(account):
      cursor.execute("SELECT * FROM sample WHERE account = {0}".format(account))
      if cursor.fetchall():
            return True
      else:
            return False

def get_pin(account):
      try:
            cursor.execute("SELECT pin FROM sample WHERE account = {0}".format(account,))
            return cursor.fetchone()[0]
      except:
            return ''

def get_balance(account):
      try:
            cursor.execute("SELECT balance FROM sample WHERE account = {0}".format(account))
            return cursor.fetchone()[0]
      except:
            return ''

def get_phone(account):
      try:
            cursor.execute("SELECT phone FROM sample WHERE account = {0}".format(account))
            return cursor.fetchone()[0]
      except:
            return ''

def set_pin(acc, pin):
      query = "UPDATE sample SET pin = {0} WHERE account = {1}"
      cursor.execute(query.format(pin, acc))
      db.commit()

def set_balance(acc, amt):
      query = "UPDATE sample SET balance = {0} WHERE account = {1}"
      cursor.execute(query.format(amt, acc))
      db.commit()
