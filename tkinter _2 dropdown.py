from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Pro Planner")
win.iconbitmap("icon.ico")
win.geometry("800x500")

var=StringVar()

com= ttk.Combobox(win)
com['state']=('readonly')
com['values']=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
com.current(0)
com.place(x=10,y=10)
win.mainloop()