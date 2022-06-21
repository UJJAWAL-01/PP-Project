from notifypy import Notify
import time
import sched

notification = Notify()
notification.title = "Productivity Manager"

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

i=0
while (i>len(keys)):
    local_time = float(values[i])
    local_time = local_time * 60
    time.sleep(local_time)

    notification.message = "It is time for your "+ keys[i]
    notification.send()
    i=i+1
    
    

#print("What shall I remind you about?")
#s = str(input())
#print("In how many minutes?")
#local_time = float(input())
#local_time = local_time * 60
#time.sleep(local_time)

#notification = Notify()
#notification.title = "Productivity Manager"
#notification.message = "It is time for your "+ s 
#notification.send()
