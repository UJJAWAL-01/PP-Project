import time
import schedule
from notifypy import Notify

#Made Lists and Dictionary to store date,time,tasks and number of tasks
timetable = {}
keys = []
task = []
days=[]
no_of_tasks=[]

#To input number of days,day and number of tasks for that day.
j=0
while(j==0):
    n=int(input("Enter number of days from 1 to 7: "))

    if(n<0 or n>7):
        print("Invalid. Please do as stated above!!!")
        continue 

    for i in range(n):
        day=input("Enter day: ")
        day=day.lower()
        days.append(day)
        num = int(input("enter the number of tasks on " + days[i]+": "))
        no_of_tasks.append(num)
        j=1

#To input the time and task
for i in range(len(days)):
    for j in range(no_of_tasks[i]):
        t = input("Enter the time on "+days[i]+": ")
        keys.append(t)
        w = input("Enter the task: ")
        task.append(w)

#Storing time and task values in dictionary
for i in range(len(keys)):
    timetable[keys[i]] = task[i]


for i in range(len(keys)):
    print("You have "+ task[i] +" in " + keys[i])

#Function for notification
def notification(task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+task
    notification.send()

#Scheduling notifications
i=0
while i<len(keys):
    schedule.every().day.at(keys[i]).do(notification,task[i])
    i=i+1


while True:
    schedule.run_pending()
    time.sleep(1)