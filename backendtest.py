import time
import schedule
from tkinter import *
from tkinter.font import BOLD
from notifypy import Notify

#Made Lists and Dictionary to store date,time,tasks and number of tasks
days=[]
no_of_tasks=[]

sunday={}
sunday_task=[]
sunday_time=[]

monday={}
monday_task=[]
monday_time=[]

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



#To input number of days,day and number of tasks for that day.
def fun():
    j=0
    n=int(ent1.get())
    if(n<0 or n>7):
        print("Invalid. Please do as stated above!!!")
    print(n)

    ''' while(j==0):
        #  n=int(input("Enter number of days from 1 to 7: "))
        n=int(ent1.get())
        if(n<0 or n>7):
            print("Invalid. Please do as stated above!!!")
            continue 

        for i in range(n):
            day=input("Enter day: ")
            day=day.lower()
            days.append(day)
            num = int(input("enter the number of tasks on " + days[i]+": "))
            no_of_tasks.append(num)
            j=1'''
#Buttons
btn= Button(win,text="Submit",width=7,command=fun)
btn.place(x=75,y=220)
win.mainloop()

#To input the time and task
for i in range(len(days)):
    for j in range(no_of_tasks[i]):

        if days[i]=="monday":
            t = input("Enter the time on "+days[i]+": ")
            monday_time.append(t)
            w = input("Enter the task: ")
            monday_task.append(w)
            for k in range(len(monday_time)):
                monday[monday_time[k]] = monday_task[k]

        if days[i]=="tuesday":
            t = input("Enter the time on "+days[i]+": ")
            tuesday_time.append(t)
            w = input("Enter the task: ")
            tuesday_task.append(w)
            for k in range(len(tuesday_time)):
                tuesday[tuesday_time[k]] = tuesday_task[k]

        if days[i]=="wednesday":
            t = input("Enter the time on "+days[i]+": ")
            wednesday_time.append(t)
            w = input("Enter the task: ")
            wednesday_task.append(w)
            for k in range(len(wednesday_time)):
                wednesday[wednesday_time[k]] = wednesday_task[k]

        if days[i]=="thursday":
            t = input("Enter the time on "+days[i]+": ")
            thursday_time.append(t)
            w = input("Enter the task: ")
            thursday_task.append(w)
            for k in range(len(thursday_time)):
                thursday[thursday_time[k]] = thursday_task[k]

        if days[i]=="friday":
            t = input("Enter the time on "+days[i]+": ")
            friday_time.append(t)
            w = input("Enter the task: ")
            friday_task.append(w)
            for k in range(len(friday_time)):
                friday[friday_time[k]] = friday_task[k]

        if days[i]=="saturday":
            t = input("Enter the time on "+days[i]+": ")
            saturday_time.append(t)
            w = input("Enter the task: ")
            saturday_task.append(w)
            for k in range(len(saturday_time)):
                saturday[saturday_time[k]] = saturday_task[k]

        if days[i]=="sunday":
                t = input("Enter the time on "+days[i]+": ")
                sunday_time.append(t)
                w = input("Enter the task: ")
                sunday_task.append(w)
                for k in range(len(sunday_time)):
                    sunday[sunday_time[k]] = sunday_task[k]

if monday:
    print("Your timetable for monday is ",monday)

if tuesday:
    print("Your timetable for tuesday is ",tuesday)

if wednesday:
    print("Your timetable for wednesday is ",wednesday)

if thursday:
    print("Your timetable for thursday is ",thursday)

if friday:
    print("Your timetable for friday is ",friday)

if saturday:
    print("Your timetable for saturday is ",saturday)

if sunday:
    print("Your timetable for Sunday is ",sunday)

#Function for notification
def monday_notification(monday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+monday_task
    notification.send()

def tuesday_notification(tuesday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+tuesday_task
    notification.send()

def wednesday_notification(wednesday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+wednesday_task
    notification.send()

def thursday_notification(thursday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+thursday_task
    notification.send()

def friday_notification(friday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+friday_task
    notification.send()

def saturday_notification(saturday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+saturday_task
    notification.send()

def sunday_notification(sunday_task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+sunday_task
    notification.send()

#Scheduling notifications
if(monday):
    i=0
    while i<len(monday_time):
        schedule.every().monday.at(monday_time[i]).do(monday_notification,monday_task[i])
        i=i+1

if(tuesday):
    i=0
    while i<len(tuesday_time):
        schedule.every().tuesday.at(tuesday_time[i]).do(tuesday_notification,tuesday_task[i])
        i=i+1

if(wednesday):
    i=0
    while i<len(wednesday_time):
        schedule.every().wednesday.at(wednesday_time[i]).do(wednesday_notification,wednesday_task[i])
        i=i+1

if(thursday):
    i=0
    while i<len(thursday_time):
        schedule.every().thursday.at(thursday_time[i]).do(thursday_notification,thursday_task[i])
        i=i+1

if(friday):
    i=0
    while i<len(friday_time):
        schedule.every().friday.at(friday_time[i]).do(friday_notification,friday_task[i])
        i=i+1

if(saturday):
    i=0
    while i<len(saturday_time):
        schedule.every().saturday.at(saturday_time[i]).do(saturday_notification,saturday_task[i])
        i=i+1

if(sunday):
    i=0
    while i<len(sunday_time):
        schedule.every().sunday.at(sunday_time[i]).do(sunday_notification,sunday_task[i])
        i=i+1

'''while True:
    schedule.run_pending()
    time.sleep(1)'''


