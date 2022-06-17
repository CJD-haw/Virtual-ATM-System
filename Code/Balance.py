from tkinter import (Label, Button, PhotoImage, Frame)
from Initial import *

class BBalance():
      def __init__(self, root, BALANCE):
            self.operation = None
            self.root = root
            self.offset = '  '*3
            self.balance = BALANCE

            self.frame = Frame(self.root, bg='#5571ff', width=1366, height=768)
            self.frame.place(x=0, y=0)
            
            self.bg = PhotoImage(file="res/bbalance.png")
            Label(self.frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            self.HOME = Button(self.frame, text="HOME")
            button(self.HOME, 1180, 370, L_GREEN, D_GREEN, WHITE, 10, 1)

            self.EXIT = Button(self.frame, text="EXIT")
            button(self.EXIT, 1180, 470, L_RED, D_RED, WHITE, 10, 1)
      
      def option(self, value):
            self.operation = value

      def show(self):               
            self.HOME.config(command=lambda: self.option('home from bbalance'))
            self.EXIT.config(command=lambda: self.option('exit from bbalance'))
            
            self.lab = Label(self.frame, text=self.balance, fg=WHITE, bg="#5571ff")            
            self.lab.place(x=600, y=250)
            self.lab.config(font = ("Helvetica", 50, "bold"))

            while not self.operation:
                  pass
            else:
                  return self.operation
            
class DBalance():
      def __init__(self, root, AMT, BALANCE):
            self.operation = None
            self.root = root
            self.offset = '  '*3
            self.amt = AMT
            self.balance = BALANCE

            self.frame = Frame(self.root, bg='#5571ff', width=1366, height=768)
            self.frame.place(x=0, y=0)
            
            self.bg = PhotoImage(file="res/dbalance.png")
            Label(self.frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            self.HOME = Button(self.frame, text="HOME")
            button(self.HOME, 1180, 370, L_GREEN, D_GREEN, WHITE, 10, 1)

            self.EXIT = Button(self.frame, text="EXIT")
            button(self.EXIT, 1180, 470, L_RED, D_RED, WHITE, 10, 1)
            
      def option(self, value):
            self.operation = value

      def show(self):               
            self.HOME.config(command=lambda: self.option('home from dbalance'))
            self.EXIT.config(command=lambda: self.option('exit from dbalance'))
            
            self.lab = Label(self.frame, text=self.balance, fg=WHITE, bg="#5571ff")            
            self.lab.place(x=600, y=250)
            self.lab.config(font = ("Helvetica", 50, "bold"))
            
            self.lab = Label(self.frame, text=self.amt, fg=WHITE, bg="#5571ff")            
            self.lab.place(x=600, y=525)
            self.lab.config(font = ("Helvetica", 50, "bold"))
            
            while not self.operation:
                  pass
            else:
                  return self.operation