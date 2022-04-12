task_status={}
n=int(input("enter the how many task"))
i=0
while i<n:
    t=input("enter the task")
    s=input("enter the status")
    task_status.update({t:s})
    print(task_status)
    i=i+1
c=0
l=len(task_status)
while c<l:
    c=c+1
user=input("what you want to do\n1)add\n2)remove\n3)edit")
print("")
if user=="add":
        task1=input("enter the task u want to add")
        status2=input("enter the status u want to add")
        task_status.update({task1:status2})
        print(task_status)
c=0
l=len(task_status)
while c<l:
    c=c+1
user1=input("what you want to do\n1)add\n2)remove\n3)edit")
if user1=="remove":
        task3=input("enter the task u want to remove")
        status4=input("enter the status u want to remove")
        del(task_status[task3])
        print(task_status)
c=0
l=len(task_status)
while c<l:
    c=c+1
user1=input("what you want to do\n1)add\n2)remove\n3)edit")
if user1=="edit":
        task7=input("enter the task u want to edit")
        status8=input("enter the status u want to edit")
        task_status.update({task7:status8})
        print(task_status)







