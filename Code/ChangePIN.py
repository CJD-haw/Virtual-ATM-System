from tkinter import (Label, Button, PhotoImage, Frame)
from Initial import *

class ChangePinNumber():
      count = 2
      def __init__(self, root):
            self.operation = None
            self.root = root
            self.offset = ' '
            self.pin = ''

            self.frame = Frame(self.root, bg='#5571ff', width=1366, height=768)
            self.frame.place(x=0, y=0)
            
            self.bg = PhotoImage(file="res/change.png")
            Label(self.frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
            
            self.CONFIRM = Button(self.frame, text="CONFIRM")
            button(self.CONFIRM, 1180, 370, L_GREEN, D_GREEN, WHITE, 10, 1)
            
            self.HOME = Button(self.frame, text="HOME")  
            button(self.HOME, 1180, 470, L_GREEN, D_GREEN, WHITE, 10, 1)
            
            self.labels()
            self.buttons()

      def option(self, value):
            self.operation = value
      
      def labels(self):
            self.labc = Label(self.frame, text=' '*28, font=FF, fg=WHITE, bg=D_BLUE)
            self.labc.place(x=540, y=40)
            self.lab0 = Label(self.frame, text=' '*28, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab0.place(x=560, y=220)
            self.lab1 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab2 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab3 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            self.lab4 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=D_BLUE)
            xo, yo = 570, 220
            self.lab1.place(x=xo, y=yo)
            self.lab2.place(x=xo+50, y=yo)
            self.lab3.place(x=xo+100, y=yo)
            self.lab4.place(x=xo+150, y=yo)
            
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
                  if len(self.pin) >= 4:
                        pass
                  else:
                        self.pin += value
            labs = (self.lab1, self.lab2, self.lab3, self.lab4)
            if value == 'X':
                  lab = labs[len(self.pin)-1]
                  lab.config(text=self.offset)
                  self.pin = self.pin[:-1]
            elif value == 'C':
                  for lab in labs:
                        lab.config(text=self.offset)
                  self.pin = ''
            else:
                  val = '  {}  '
                  i = len(self.pin)-1
                  lab = labs[i]
                  lab.config(text=val.format(self.pin[i]))

      def show(self):      
            self.CONFIRM.config(command=lambda: self.option('confirm from change pin'))
            self.HOME.config(command=lambda: self.option('home from change pin'))
            self.labc.config(text=' {0} Attemps You Have '.format(ChangePinNumber.count+1))
            
            while not self.operation:
                  pass
            
            if self.operation == 'home from change pin':
                  ChangePinNumber.count = 2
                  return self.operation, ''
            elif self.operation == 'confirm from change pin':
                  if len(self.pin) == 4 and ChangePinNumber.count:
                        return self.operation, self.pin
                  elif ChangePinNumber.count:
                        ChangePinNumber.count -= 1
                        return 'invalid from change pin', ''
                  else:
                        ChangePinNumber.count = 2
                        return 'wrong from change pin', ''
