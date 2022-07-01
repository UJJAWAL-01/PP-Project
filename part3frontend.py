import time
import schedule
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from notifypy import Notify

#Made Lists and Dictionary to store date,time,tasks and number of tasks
days=[]
no_of_tasks=[]

sunday={}
sunday_task=[]
sunday_time=[]

MONDAY={}
MONDAY_task=[]
MONDAY_time=[]

tuesday={}
tuesday_task=[]
tuesday_time=[]

wednesday={}
wednesday_task=[]
wednesday_time=[]

thursday={}
thursday_task=[]
thursday_time=[]

friday={}
friday_task=[]
friday_time=[]

saturday={}
saturday_task=[]
saturday_time=[]

win=Tk()
win.title("Pro Planner")
win.geometry("800x500")

#Label and entry
lbl1=Label(win,text="Enter number of days(1-7) ",bg="sky blue",fg="black",width=25,height=2,font=("Arial",11,BOLD))
lbl1.place(x=20,y=20)
ent1=Entry(win,bg="white",fg="black",bd=10,font=("Arial",11),width=20)
ent1.place(x=260,y=20)

lbl3=Label(win,text="Enter number of tasks",bg="sky blue",fg="black",width=25,height=2,font=("arial",11,BOLD))
lbl3.place(x=20,y=120)
ent3=Entry(win,bg="white",fg="black",bd=10,font=("Arial",11),width=20)
ent3.place(x=260,y=120)


def printVal(li,task):
    for i in li:
        print(i.get(),end="\t\t")
    print("")
    for j in range(int(ent3.get())):
        for i in range(int(ent1.get())):
            print(task[i][j].get(),end='\t')
        print("")

def input_number():
    n=int(ent1.get())
    if(n not in range (0,7)):
        lbl5=Label(win,text="Invalid Number. Start Again",bg="sky blue",fg="black",width=25,height=2,font=("Arial",11,BOLD))
        lbl5.place(x=20,y=270)
    else:
        next = Toplevel(win)
        next.title("Pro Planner")
        next.geometry("800x500")
        days = []
        no_of_task = []
    
        for i in range(int(ent1.get())):
            a = []
            for j in range(int(ent3.get())):
                a.append(StringVar())               #Here we use stringvar variable in ord
            no_of_task.append(a)
        for i in range(int(ent1.get())):
            days.append(StringVar())
        for i in range(int(ent1.get())):
            a = Entry(next,textvariable=days[i])
            a.grid(row=0,column=i)
        for i in range(int(ent1.get())):
            for j in range(int(ent3.get())):
                a = Entry(next,textvariable=no_of_task[i][j])
                a.grid(row=1+j,column=i)

        ttk.Button(next, text="see", command=lambda: printVal(days,no_of_task)).grid(row=int(ent3.get())+1,column=0)


btn= ttk.Button(win,text="Next",width=7,command=input_number)
btn.place(x=520,y=20)
win.mainloop()
