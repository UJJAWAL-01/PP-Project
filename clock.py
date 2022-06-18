from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('CLOCK')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 36, 'bold'),
            background='sky blue',
            foreground='white')

lbl.pack(anchor = 'center')
time()
mainloop()


