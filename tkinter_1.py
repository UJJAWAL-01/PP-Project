from tkinter import *

win=Tk()
win.title("Pro Planner")
win.iconbitmap("icon.ico")
win.geometry("800x500")
#function
def func():
    var.get()
    lbl2.config(text=var.get(),fg="red")
    
    
#label
lbl1=Label(win,text="User Name:",bg="black",fg="white",width=10,height=1)
lbl1.place(x=10,y=10)


lbl2=Label(win,fg="black",width=10,height=1)
lbl2.place(x=20,y=150)


#entry
var=StringVar()
ent1=Entry(win,bg="white",fg="black",bd=5,font=("Arial",10),width=15,textvariable=var)
ent1.place(x=95,y=10)


#button
btn=Button(win,text="Submit",bg="white",fg="black",command=func)
btn.place(x=10,y=110)


win.mainloop()
