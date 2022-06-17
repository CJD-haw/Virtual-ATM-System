from tkinter import (Label, PhotoImage, Frame)
from time import sleep

class Greet():
      def __init__(self, root, img):
            self.cx, self.cy = None, None
            self.root = root
            root.bind('<ButtonPress-1>', self.on_click)
            
            self.frame = Frame(root, bg='#5571ff', width=1366, height=768)
            self.frame.place(x=0, y=0)
            
            self.bg1 = PhotoImage(file="res/{0}_01.png".format(img))
            self.bg2 = PhotoImage(file="res/{0}_02.png".format(img))
            self.bg3 = PhotoImage(file="res/{0}_03.png".format(img))
            self.bg4 = PhotoImage(file="res/{0}_04.png".format(img))
            
      def show(self):
            while self.cx is None and self.cy is None:
                  for bg in self.bg1, self.bg2, self.bg3, self.bg4:
                        Label(self.frame, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
                        if self.cx is not None and self.cy is not None:
                              break
                        sleep(0.5)

      def on_click(self, event):
            self.cx, self.cy = event.x, event.y
