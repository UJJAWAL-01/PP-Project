k=input("Do you have any other assignments to complete(Enter yes or no) : ")
k=k.lower()

if k=="yes":
    a=int(input("Enter number of assignments: "))
    for i in range(a):
        t=input("Enter tasks: ")
        rand_task.append(t)
if k=="no":
    exit
print(f"Your extra tasks are these {rand_task}")