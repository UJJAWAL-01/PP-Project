#To input the time and task

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
days=[]
no_of_tasks=[]

for i in range(len(days)):
    for j in range(no_of_tasks[i]):

        if days[i]=="MONDAY":
            t = input("Enter the time on "+days[i].upper()+": ")
            MONDAY_time.append(t)
            w = input("Enter the task: ")
            MONDAY_task.append(w)
            for k in range(len(MONDAY_time)):
                MONDAY[MONDAY_time[k]] = MONDAY_task[k]

        if days[i]=="TUESDAY":
            t = input("Enter the time on "+days[i].upper()+": ")
            TUESDAY_time.append(t)
            w = input("Enter the task: ")
            TUESDAY_task.append(w)
            for k in range(len(TUESDAY_time)):
                TUESDAY[TUESDAY_time[k]] = TUESDAY_task[k]

        if days[i]=="WEDNESDAY":
            t = input("Enter the time on "+days[i].upper()+": ")
            WEDNESDAY_time.append(t)
            w = input("Enter the task: ")
            WEDNESDAY_task.append(w)
            for k in range(len(WEDNESDAY_time)):
                WEDNESDAY[WEDNESDAY_time[k]] = WEDNESDAY_task[k]

        if days[i]=="THURSDAY":
            t = input("Enter the time on "+days[i].upper()+": ")
            THURSDAY_time.append(t)
            w = input("Enter the task: ")
            THURSDAY_task.append(w)
            for k in range(len(THURSDAY_time)):
                THURSDAY[THURSDAY_time[k]] = THURSDAY_task[k]

        if days[i]=="FRIDAY":
            t = input("Enter the time on "+days[i].upper()+": ")
            FRIDAY_time.append(t)
            w = input("Enter the task: ")
            FRIDAY_task.append(w)
            for k in range(len(FRIDAY_time)):
                FRIDAY[FRIDAY_time[k]] = FRIDAY_task[k]

        if days[i]=="SATURDAY":
            t = input("Enter the time on "+days[i].upper()+": ")
            SATURDAY_time.append(t)
            w = input("Enter the task: ")
            SATURDAY_task.append(w)
            for k in range(len(SATURDAY_time)):
                SATURDAY[SATURDAY_time[k]] = SATURDAY_task[k]

        if days[i]=="SUNDAY":
                t = input("Enter the time on "+days[i].upper()+": ")
                SUNDAY_time.append(t)
                w = input("Enter the task: ")
                SUNDAY_task.append(w)
                for k in range(len(SUNDAY_time)):
                    SUNDAY[SUNDAY_time[k]] = SUNDAY_task[k]


if MONDAY:
    print("Your timetable for MONDAY is ",MONDAY)
if TUESDAY:
    print("Your timetable for TUESDAY is ",TUESDAY)
if WEDNESDAY:
    print("Your timetable for WEDNESDAY is ",WEDNESDAY)
if THURSDAY:
    print("Your timetable for THURSDAY is ",THURSDAY)
if FRIDAY:
    print("Your timetable for FRIDAY is ",FRIDAY)
if SATURDAY:
    print("Your timetable for SATURDAY is ",SATURDAY)
if SUNDAY:
    print("Your timetable for SUNDAY is ",SUNDAY)