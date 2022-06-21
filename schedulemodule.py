import time
import schedule
from notifypy import Notify

work_list = {}
keys = []
values = []

tasks = int(input("enter the number of tasks: "))

for i in range(tasks):
    t = input("Enter the time: ")
    keys.append(t)
    w = input("Enter the task: ")
    values.append(w)

for i in range(len(keys)):
    work_list[keys[i]] = values[i]
print(work_list)

for i in range(len(keys)):
    print("You have "+ keys[i] +" in " + values[i])

def timetable():
    notification = Notify()
    notification.title = "Productivity Manager"
    notification.message = "It is time for your "
    notification.send()

i=0
while i<len(keys):
    schedule.every().day.at(keys[i]).do(timetable)
    i=i+1


while True:
    schedule.run_pending()
    time.sleep(1)