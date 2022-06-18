from tkinter import *
from turtle import color

root = Tk()
root.geometry("500x1000")

w = Label(root, text = 'To Do List', font = '120')
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()
Checkbutton5 = IntVar()
Checkbutton6 = IntVar()

Button1 = Checkbutton(root, text = "Task 1",
                    variable = Checkbutton1,
                    onvalue = 1,
                    offvalue = 0,
                    height = 3,
                    width = 120,
                    background='sky blue',
                    foreground='black',
                    font = '50')

Button2 = Checkbutton(root, text = "Task 2",
                    variable = Checkbutton2,
                    onvalue = 1,
                    offvalue = 0,
                    height = 3,
                    width = 120,
                    background='sky blue',
                    foreground='black',
                    font = '50')

Button3 = Checkbutton(root, text = "Task 3",
                    variable = Checkbutton3,
                    onvalue = 1,
                    offvalue = 0,
                    height = 3,
                    width = 120,
                    background='sky blue',
                    foreground='black',
                    font = '50')

Button4 = Checkbutton(root, text = "Task 4",
                    variable = Checkbutton4,
                    onvalue = 1,
                    offvalue = 0,
                    height = 3,
                    width = 120,
                    background='sky blue',
                    foreground='black',
                    font = '50')
     
Button5 = Checkbutton(root, text = "Task 5",
                    variable = Checkbutton5,
                    onvalue = 1,
                    offvalue = 0,
                    height = 3,
                    width = 120,
                    background='sky blue',
                    foreground='black',
                    font = '50')

Button6 = Checkbutton(root, text = "Task 6",
                    variable = Checkbutton6,
                    onvalue = 1,
                    offvalue = 0,
                    height = 3,
                    width = 120,
                    background='sky blue',
                    foreground='black',
                    font = '50')

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()

mainloop()