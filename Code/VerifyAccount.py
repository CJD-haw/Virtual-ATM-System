from tkinter import (Label, Button, PhotoImage, Frame)
from Initial import *
from Backend import *

class Account():
    def __init__(self, root):
        self.operation = None
        self.root = root
        self.offset = ' '
        self.account = ''

        self.frame = Frame(self.root, bg='#5571ff', width=1366, height=768)
        self.frame.place(x=0, y=0)

        self.bg = PhotoImage(file="res/ano.png")
        Label(self.frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

    def option(self, value):
        self.operation = value
        
    def labels(self):
        dbg = D_BLUE
        self.lab0 = Label(self.frame, text=' '*32, font=FF, fg=WHITE, bg=dbg)
        self.lab0.place(x=540, y=220)
        self.lab1 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab2 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab3 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab4 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab5 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab6 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab7 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab8 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab9 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab10 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab11 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        self.lab12 = Label(self.frame, text=self.offset, font=FF, fg=WHITE, bg=dbg)
        xo, yo = 570, 220
        self.lab1.place(x=xo-20, y=yo)
        self.lab2.place(x=xo+0, y=yo)
        self.lab3.place(x=xo+20, y=yo)
        self.lab4.place(x=xo+40, y=yo)
        self.lab5.place(x=xo+60, y=yo)
        self.lab6.place(x=xo+80, y=yo)
        self.lab7.place(x=xo+100, y=yo)
        self.lab8.place(x=xo+120, y=yo)
        self.lab9.place(x=xo+140, y=yo)
        self.lab10.place(x=xo+160, y=yo)
        self.lab11.place(x=xo+180, y=yo)
        self.lab12.place(x=xo+200, y=yo)

    def buttons(self):
        xo, yo, off, = 580, 280, 65
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
            if len(self.account) >= 12:
                pass
            else:
                self.account += value
        labs = (self.lab1, self.lab2, self.lab3, self.lab4, self.lab5, self.lab6, 
                self.lab7, self.lab8, self.lab9, self.lab10, self.lab11, self.lab12)
        if value == 'X':
            lab = labs[len(self.account)-1]
            lab.config(text=self.offset)
            self.account = self.account[:-1]
        elif value == 'C':
            for lab in labs:
                lab.config(text=self.offset)
                self.account = ''
        else:
            val = '{}'
            i = len(self.account)-1
            lab = labs[i]
            lab.config(text=val.format(self.account[i]))

    def show(self):
        self.note = 'Correct Account Number For Further Transaction'
        self.labc = Label(self.frame, text=self.note, font=FF, fg=WHITE, bg=D_BLUE)
        self.labc.place(x=365, y=40)

        self.CONFIRM = Button(self.frame, text="CONFIRM")
        button(self.CONFIRM, 1180, 370, L_GREEN, D_GREEN, WHITE, 10, 1)                
        self.CONFIRM.config(command=lambda: self.option('confirm from account'))

        self.EXIT = Button(self.frame, text="Exit")  
        button(self.EXIT, 1180, 470, L_RED, D_RED, WHITE, 10, 1)
        self.EXIT.config(command=lambda: self.option('exit from account'))
        
        self.labels()
        self.buttons()      
        
        while not self.operation:
            pass

        if self.operation == 'exit from account':
            return self.operation, ''
        elif self.operation == 'confirm from account':
            if len(self.account) == 12 and check_account(self.account):
                return self.operation, self.account
            else:
                return 'invalid from account', ''
