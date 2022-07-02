import time
import schedule
from notifypy import Notify

#Made Lists and Dictionary to store date,time,tasks and number of tasks
timetable = {}
task_time = []
task = []
days=[]
no_of_tasks=[]

#To input number of days,day and number of tasks for that day.
j=0
while(j==0):
    n=input('Enter number of days from 1 to 7: ')

    if(n.isnumeric()==False):
        print("Invalid. Please do as stated above!!!")
        continue 
    else:
        n=int(n)

    for i in range(n):
        while(True):
            day=input("Enter day: ")
            day=day.strip()
            if(day.isnumeric()==True or day==""):
                print("Enter the name of the day!")  
                continue  
            else:
                break
        day=day.lower()
        days.append(day)
        
        while(True):

            num = input("Enter the number of tasks on " + days[i]+": ")
            if (num.isnumeric()==False):
                print("Please enter a valid number!!")
                continue
            else:
                num=int(num)
                break
        no_of_tasks.append(num)
        j=1

#To input the time and task
for i in range(len(days)):
    for j in range(no_of_tasks[i]):
        while(True):
            t = input("Enter the time on "+days[i]+" "+ "in HH:MM format:")
            t=t.strip()
            if(t.isnumeric()==True or t==""):
                print("Enter Time in Valid Format")
                continue
            else:
                break
        task_time.append(t)
        while(True):
            w = input("Enter the task: ")
            w.strip()
            if(w.isnumeric()==True or w==""):
                print("Please enter a valid task!!")
                continue
            else:
                break

        task.append(w)

#Storing time and task values in dictionary
for i in range(len(task_time)):
    timetable[task_time[i]] = task[i]


for i in range(len(task_time)):
    print("You have "+ task[i] +" at " + task_time[i])

# Function for notification
def notification(task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+task
    notification.send()

# Scheduling notifications
i=0
while i<len(task_time):
    schedule.every().day.at(task_time[i]).do(notification,task[i])
    i=i+1


while True:
    schedule.run_pending()
    time.sleep(1)