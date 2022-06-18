

work_list = {}
keys = []
values = []

tasks = int(input("enter the number of tasks: "))

for i in range(tasks):
    t = (input("Enter the time: "))
    keys.append(t)
    w = input("Enter the task: ")
    values.append(w)


for i in range(len(keys)):
    work_list[keys[i]] = values[i]
print(work_list)