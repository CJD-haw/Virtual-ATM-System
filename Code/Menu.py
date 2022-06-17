from tkinter import (Label, Button, PhotoImage, Frame)
from Initial import (button, L_RED, L_GREEN, L_BLUE, D_RED, D_GREEN, D_BLUE, WHITE)

class Home():
      def __init__(self, root):
            self.operation = None
            self.root = root
            
            self.frame = Frame(self.root, bg='#5571ff', width=1366, height=768)
            self.frame.place(x=0, y=0)
            
            self.bg = PhotoImage(file="res/home.png")
            Label(self.frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

      def option(self, value):
            self.operation = value

      def show(self):  
            self.PIN = Button(self.frame, text="CHANGE PIN")
            self.PIN.config(command=lambda: self.option('change pin from home'))
            button(self.PIN, 1160, 270, L_GREEN, D_GREEN, WHITE, 12, 1)  

            self.DEBIT = Button(self.frame, text="WITHDRAW")
            self.DEBIT.config(command=lambda: self.option('debit from home'))
            button(self.DEBIT, 1160, 370, L_GREEN, D_GREEN, WHITE, 12, 1)  
            
            self.BALANCE = Button(self.frame, text="BALANCE")
            self.BALANCE.config(command=lambda: self.option('balance from home'))            
            button(self.BALANCE, 1160, 470, L_GREEN, D_GREEN, WHITE, 12, 1)
            
            while not self.operation:
                  pass
            else:
                  return self.operation
