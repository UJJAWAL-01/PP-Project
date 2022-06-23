from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Pro Planner")
win.iconbitmap("icon.ico")
win.geometry("800x500")

def func():
    print(checkbtn1.get())
    print(checkbtn2.get())


checkbtn1= IntVar()
checkbtn2=IntVar()

select=Checkbutton(win,text="Yes",variable=checkbtn1,onvalue=1,offvalue=0)
select.pack()


select=Checkbutton(win,text="no",variable=checkbtn2,onvalue=1,offvalue=0)
select.pack()
btn= Button(win,text="done",command=func)
btn.pack()

win.mainloop()