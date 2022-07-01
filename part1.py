#To input number of days,day and number of tasks for that day.
days=[]
no_of_tasks=[]
j=0
while(j==0):
    
    n=int(input("Enter number of days from 1 to 7: "))
    if(n<0 or n>7):
        print("Invalid. Please do as stated above!!!")
        continue
        
    for i in range(n):
            day=input("Enter day: ")
            day=day.upper()
            days.append(day)
            num = int(input("enter the number of tasks on " + days[i].upper()+": "))
            no_of_tasks.append(num)
            j=1