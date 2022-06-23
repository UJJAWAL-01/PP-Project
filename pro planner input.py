from tkinter import *

win=Tk()
win.title("Pro Planner")
win.iconbitmap("icon.ico")
win.geometry("800x500")
#Label
lbl1=Label(win,text="Enter days(1-7) ",bg="black",fg="white",width=12,height=1)
lbl1.place(x=10,y=10)

lbl2=Label(win,text="Enter day",bg="black",fg="white",width=12,height=1)
lbl2.place(x=10,y=50)

lbl2=Label(win,text="Enter no of tasks",bg="black",fg="white",width=12,height=1)
lbl2.place(x=10,y=90)

lbl2=Label(win,text="Enter time",bg="black",fg="white",width=12,height=1)
lbl2.place(x=10,y=130)


#Entry Box
ent1=Entry(win,bg="white",fg="black",bd=5,font=("Arial",10),width=15)
ent1.place(x=115,y=10)

ent2=Entry(win,bg="white",fg="black",bd=5,font=("Arial",10),width=15)
ent2.place(x=115,y=50)

ent2=Entry(win,bg="white",fg="black",bd=5,font=("Arial",10),width=15)
ent2.place(x=115,y=90)

ent2=Entry(win,bg="white",fg="black",bd=5,font=("Arial",10),width=15)
ent2.place(x=115,y=130)

#Buttons
btn=Button(win,text="Submit",bg="white",fg="black")
btn.place(x=50,y=180)

win.mainloop()