from tkinter import *
from tkinter.ttk import Progressbar
import tkinter as tk
import time
class __PROCESS__(tk.Tk):        
    def process(self):
        for i in range(self.length):
            self.update_idletasks()
            self.pb['value'] += 1
            time.sleep(0.001)
            self.txt['text']=self.pb['value'],'%'
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('PythonGuides')
        self.geometry('200x150')
        self.config(bg='#345')
        
        
        self.length=100 # length process
        
        
        self.pb=Progressbar(
            self,
            orient = HORIZONTAL,
            length = self.length,
            mode = 'determinate'
            )
        self.pb.place(x=40, y=20)
        self.txt=tk.Label(
            self,
            text = '0%',
            bg = '#345',
            fg = 'light green'
        )
        self.txt.place(x=150 ,y=20)
        self.bnt=tk.Button(
            self,
            text='Start',
            command=self.process
        ).place(x=40, y=50)
        self.mainloop()
if __name__=='__main__':
    __PROCESS__()
