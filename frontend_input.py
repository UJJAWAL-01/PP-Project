from tkinter import *
from tkinter.font import BOLD

win=Tk()
win.title("Pro Planner")
win.geometry("800x500")

#Label
lbl1=Label(win,text="Enter number of days(1-7) ",bg="sky blue",fg="black",width=25,height=2,font=("Arial",11,BOLD))
lbl1.place(x=20,y=20)

lbl2=Label(win,text="Enter day",bg="sky blue",fg="black",width=25,height=2,font=("Arial",11,BOLD))
lbl2.place(x=20,y=70)

lbl2=Label(win,text="Enter number of tasks",bg="sky blue",fg="black",width=25,height=2,font=("arial",11,BOLD))
lbl2.place(x=20,y=120)

lbl2=Label(win,text="Enter time",bg="sky blue",fg="black",width=25,height=2,font=("arial",11,BOLD))
lbl2.place(x=20,y=170)

#Entry Box
ent1=Entry(win,bg="white",fg="black",bd=10,font=("Arial",11),width=20)
ent1.place(x=260,y=20)

ent2=Entry(win,bg="white",fg="black",bd=10,font=("Arial",11),width=20)
ent2.place(x=260,y=70)

ent3=Entry(win,bg="white",fg="black",bd=10,font=("Arial",11),width=20)
ent3.place(x=260,y=120)

ent4=Entry(win,bg="white",fg="black",bd=10,font=("Arial",11),width=20)
ent4.place(x=260,y=170)

#Buttons
btn=Button(win,text="Submit",bg="white",fg="black",height=1,width=7)
btn.place(x=75,y=220)

win.mainloop()