#Modules used for functionality
import time
import schedule
from notifypy import Notify
import random
import pandas as pd

#Made Lists and Dictionary to store date,time,tasks and number of tasks
days=[]
no_of_tasks=[]
rand_task=[]

SUNDAY={}
SUNDAY_task=[]
SUNDAY_time=[]

MONDAY={}
MONDAY_task=[]
MONDAY_time=[]

TUESDAY={}
TUESDAY_task=[]
TUESDAY_time=[]

WEDNESDAY={}
WEDNESDAY_task=[]
WEDNESDAY_time=[]

THURSDAY={}
THURSDAY_task=[]
THURSDAY_time=[]

FRIDAY={}
FRIDAY_task=[]
FRIDAY_time=[]

SATURDAY={}
SATURDAY_task=[]
SATURDAY_time=[]

#To input number of days,name of the day and number of tasks for that day.

j=0
while(j==0):    
    n=input("Enter number of days from 1 to 7: ")
    if(n.isnumeric()==False):
        print("Invalid. Please do as stated above!!!")
        continue 
    else:
        n=int(n)
        
    for i in range(int(n)):
            day=input("Enter the day: ")
            day=day.upper()
            days.append(day)
            e=0
            while e==0:
                num = input("Enter the number of tasks on " + days[i].upper()+": ")
                if (num.isnumeric()==False):
                    print("Please enter a valid number!!")
                    continue
                else:
                    no_of_tasks.append(int(num))
                e=1
            j=1


#To input the time and task
for i in range(len(days)):
    for j in range(no_of_tasks[i]):
        if days[i]=="MONDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                MONDAY_time.append(t)
                w = input("Enter the task: ")
                MONDAY_task.append(w)
                MONDAY["Time "]=MONDAY_time
                MONDAY["  Task"]=MONDAY_task
        
        if days[i]=="TUESDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                TUESDAY_time.append(t)
                w = input("Enter the task: ")
                TUESDAY_task.append(w)
                TUESDAY["Time "]=TUESDAY_time
                TUESDAY["  Task"]=TUESDAY_task

        if days[i]=="WEDNESDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                WEDNESDAY_time.append(t)
                w = input("Enter the task: ")
                WEDNESDAY_task.append(w)
                WEDNESDAY["Time "]=WEDNESDAY_time
                WEDNESDAY["  Task"]=WEDNESDAY_task

        if days[i]=="THURSDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                THURSDAY_time.append(t)
                w = input("Enter the task: ")
                THURSDAY_task.append(w)
                THURSDAY["Time "]=THURSDAY_time
                THURSDAY["  Task"]=THURSDAY_task

        if days[i]=="FRIDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                FRIDAY_time.append(t)
                w = input("Enter the task: ")
                FRIDAY_task.append(w)
                FRIDAY["Time "]=FRIDAY_time
                FRIDAY["  Task"]=FRIDAY_task

        if days[i]=="SATURDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                SATURDAY_time.append(t)
                w = input("Enter the task: ")
                SATURDAY_task.append(w)
                SATURDAY["Time "]=SATURDAY_time
                SATURDAY["  Task"]=SATURDAY_task
        
        if days[i]=="SUNDAY":
                t = input(f"Enter the time for task on {days[i].upper()} (in 24 hour format) : ")
                SUNDAY_time.append(t)
                w = input("Enter the task: ")
                SUNDAY_task.append(w)
                SUNDAY["Time "]=SUNDAY_time
                SUNDAY["  Task"]=SUNDAY_task

        if days[i]!="MONDAY" and days[i]!="TUESDAY" and days[i]!="WEDNESDAY" and days[i]!="THURSDAY" and days[i]!="FRIDAY" and days[i]!="SATURDAY" and days[i]!="SUNDAY":
            print(days[i]+ ": This day of the week does not exist!!!")


if MONDAY:
    dfmon=pd.DataFrame(MONDAY)
    print(f"\n\nYour time table for MONDAY is: \n{dfmon}")
if TUESDAY:
    dftue=pd.DataFrame(TUESDAY)
    print(f"\n\nYour time table for TUESDAY is: \n{dftue}")
if WEDNESDAY:
    dfwed=pd.DataFrame(WEDNESDAY)
    print(f"\n\nYour time table for WEDNESDAY is: \n{dfwed}")
if THURSDAY:
    dfthur=pd.DataFrame(THURSDAY)
    print(f"\n\nYour time table for THURSDAY is: \n{dfthur}")
if FRIDAY:
    dffri=pd.DataFrame(FRIDAY)
    print(f"\n\nYour time table for FRIDAY is: \n{dffri}")
if SATURDAY:
    dfsat=pd.DataFrame(SATURDAY)
    print(f"\n\nYour time table for SATURDAY is: \n{dfsat}")
if SUNDAY:    
    dfsun=pd.DataFrame(SUNDAY)
    print(f"\n\nYour time table for SUNDAY is: \n{dfsun}")

# Input extra assignments to complete and randomly suggest using random module.

z=0
while z==0:
    k=input("Do you have any other assignments to complete(Enter yes or no) : ")
    k=k.lower()
    if k=="yes":
        a=int(input("Enter number of assignments: "))
        for i in range(a):
            t=input("Enter tasks: ")
            rand_task.append(t)
        print(f"Your extra assignments are, {rand_task}")
        z=1
    if k=="no":
        rand_task.append(" ")
        z=1
    if k!="yes" and k!="no":
        print('''Please type "Yes" or "No" ''')
        continue
random_num=random.choice(rand_task)

#Function for notification and random task suggesting

def MONDAY_notification(MONDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {MONDAY_task} \nDo remember to complete {random_num}"
    else:
        notification.message = "It is time for "+ MONDAY_task
    notification.send()

def TUESDAY_notification(TUESDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {TUESDAY_task} \nDo remember to complete the {random_num}"
    else:
        notification.message = "It is time for "+ TUESDAY_task
    notification.send()

def WEDNESDAY_notification(WEDNESDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {WEDNESDAY_task} \nDo remember to complete the {random_num}"
    else:
        notification.message = "It is time for "+ WEDNESDAY_task
    notification.send()

def THURSDAY_notification(THURSDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {THURSDAY_task} \nDo remember to complete the {random_num}"
    else:
        notification.message = "It is time for "+ THURSDAY_task
    notification.send()

def FRIDAY_notification(FRIDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {FRIDAY_task} \nDo remember to complete the {random_num}"
    else:
        notification.message = "It is time for "+ FRIDAY_task
    notification.send()

def SATURDAY_notification(SATURDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {SATURDAY_task} \nDo remember to complete the {random_num}"
    else:
        notification.message = "It is time for "+ SATURDAY_task
    notification.send()

def SUNDAY_notification(SUNDAY_task):
    notification = Notify()
     
    notification.title = "Productivity Manager"
    if k=="yes":
        notification.message = f"It is time for {SUNDAY_task} \nDo remember to complete the {random_num}"
    else:
        notification.message = "It is time for "+ SUNDAY_task
    notification.send()

#Scheduling notifications

if(MONDAY):
    i=0
    while i<len(MONDAY_time):
        schedule.every().monday.at(MONDAY_time[i]).do(MONDAY_notification,MONDAY_task[i])
        i=i+1
if(TUESDAY):
    i=0
    while i<len(TUESDAY_time):
        schedule.every().tuesday.at(TUESDAY_time[i]).do(TUESDAY_notification,TUESDAY_task[i])
        i=i+1
if(WEDNESDAY):
    i=0
    while i<len(WEDNESDAY_time):
        schedule.every().wednesday.at(WEDNESDAY_time[i]).do(WEDNESDAY_notification,WEDNESDAY_task[i])
        i=i+1
if(THURSDAY):
    i=0
    while i<len(THURSDAY_time):
        schedule.every().thursday.at(THURSDAY_time[i]).do(THURSDAY_notification,THURSDAY_task[i])
        i=i+1
if(FRIDAY):
    i=0
    while i<len(FRIDAY_time):
        schedule.every().friday.at(FRIDAY_time[i]).do(FRIDAY_notification,FRIDAY_task[i])
        i=i+1
if(SATURDAY):
    i=0
    while i<len(SATURDAY_time):
        schedule.every().saturday.at(SATURDAY_time[i]).do(SATURDAY_notification,SATURDAY_task[i])
        i=i+1
if(SUNDAY):
    i=0
    while i<len(SUNDAY_time):
        schedule.every().sunday.at(SUNDAY_time[i]).do(SUNDAY_notification,SUNDAY_task[i])
        i=i+1

while True:
    schedule.run_pending()
    time.sleep(1)
