elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[]
b=[]
sum=0
sum1=0
while i<len(elements):
    j=elements[i]
    if j%2==0:
        a.append(j)
        sum=sum+j
    else:
        b.append(j)
        sum1=sum+j
    i=i+1 
print("even numbers",a,sum)
print("odd numbers",b,sum1)








