list1=[1,2,3,4,5,6,7,8,9,11,13]
list2=[]
for j in list1:
    i=1
    c=0
    while i<=j:
        if j%i==0:
            c=c+1
        i=i+1
    if c==2:
        list2.append(j)
print(list2)    

