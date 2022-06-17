from tkinter import (Label, Button, PhotoImage, Frame)
from Initial import *

class Debit():
      def __init__(self, root, AMT):
            self.operation = None
            self.root = root
            self.AMT = AMT
            self.offset = ' '*6
            self.amt = ''

            self.frame = Frame(self.root, bg='#5571ff', width=1366, height=768)
            self.frame.place(x=0, y=0)
            
            self.bg = PhotoImage(file="res/debit.png")
            Label(self.frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
      
      def option(self, value):
            self.operation = value
      
      def show(self):
            self.note = 'Debiting Amount from 500 to 10000 Only Allowed'
            self.labc = Label(self.frame, text=self.note, font=FF, fg=WHITE, bg=D_BLUE)
            self.labc.place(x=365, y=40)
            self.lab1 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab2 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab3 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab4 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab5 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            xo, yo = 570, 220
            self.lab1.place(x=xo, y=yo)
            self.lab2.place(x=xo+40, y=yo)
            self.lab3.place(x=xo+80, y=yo)
            self.lab4.place(x=xo+120, y=yo)
            self.lab5.place(x=xo+160, y=yo)

            self.CONFIRM = Button(self.frame, text="CONFIRM")
            self.CONFIRM.config(command=lambda: self.option('confirm from debit'))
            button(self.CONFIRM, 1180, 370, L_GREEN, D_GREEN, WHITE, 10, 1)

            self.HOME = Button(self.frame, text="HOME")
            self.HOME.config(command=lambda: self.option('home from debit'))
            button(self.HOME, 1180, 470, L_GREEN, D_GREEN, WHITE, 10, 1)
            
            self.buttons()

            while not self.operation:
                  pass
            if self.operation == 'home from debit':
                  return self.operation, '', ''
            elif self.operation == 'confirm from debit':
                  if int(self.AMT) >= int(self.amt) and self.operation == 'confirm from debit':
                        if int(self.amt)%500 is 0 and int(self.amt) <= 10000:
                              self.AMT = int(self.AMT) - int(self.amt)
                              if self.AMT >= 500:
                                    return self.operation, self.amt, str(self.AMT)
            return 'insufficient balance', '', ''
      
      def buttons(self):
            xo, yo, off = 580, 280, 65
            num = (('7', '8', '9'), ('4', '5', '6'), ('1', '2', '3'), ('X', '0', 'C'))
            for row in (0, 1, 2, 3):
                  for col in (0, 1, 2):
                        b = Button(self.frame, text=num[row][col])
                        b.config(command=lambda v=num[row][col]:self.enter(v))
                        if row is 3 and col in (0, 2):
                              button(b, xo+off*col, yo+off*row, L_RED, D_RED, WHITE, 3, 1)
                        else:
                              button(b, xo+off*col, yo+off*row, L_GREEN, D_GREEN, WHITE, 3, 1)

      def enter(self, value):
            if value in '0123456789':
                  if len(self.amt) >= 5:
                        pass
                  else:
                        self.amt += value
            labs = (self.lab1, self.lab2, self.lab3, self.lab4, self.lab5)
            if value == 'X':
                  amt = self.amt
                  lab = labs[len(amt)-1]
                  lab.config(text=self.offset)
                  self.amt = self.amt[:-1]
            elif value == 'C':
                  for lab in labs:
                        lab.config(text=self.offset)
                  self.amt = ''
            else:
                  amt = self.amt
                  val = '  {}  '
                  i = len(amt)-1
                  lab = labs[i]
                  lab.config(text=val.format(amt[i]))
