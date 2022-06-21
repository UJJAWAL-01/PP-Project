from notifypy import Notify
import time

print("What shall I remind you about?")
s = str(input())
print("In how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)

notification = Notify()
notification.title = "Productivity Manager"
notification.message = "It is time for your "+ s 
notification.send()