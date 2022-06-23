import time
import schedule
from notifypy import Notify

timetable = {}
keys = []
task = []
no_of_tasks=[]

n=int(input("Enter number of days from 1 to 7: "))
days=[]

if(n>0 and n<=7):
    for i in range(n):
        day=input("Enter day: ")
        days.append(day)
        num = int(input("enter the number of tasks on " + days[i]+": "))
        no_of_tasks.append(num)
else:
        print("Please input number of days from 1-7!!")

for i in range(len(days)):
    for j in range(len(no_of_tasks)-1):
        t = input("Enter the time on "+days[i]+": ")
        keys.append(t)
        w = input("Enter the task: ")
        task.append(w)

for i in range(len(keys)):
    timetable[keys[i]] = task[i]


for i in range(len(keys)):
    print("You have "+ task[i] +" in " + keys[i])

def notification(task):
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "+task
    notification.send()

i=0
while i<len(keys):
    schedule.every().day.at(keys[i]).do(notification,task[i])
    i=i+1


while True:
    schedule.run_pending()
    time.sleep(1)
