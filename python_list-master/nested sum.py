a=[[0],[1,3],[5,7],67,[9,8],[12,15,17],98]
i=0
sum=0
while i<len(a):
    b=a[i]
    if type (b) is list:
        for  j in range (len(b)):
            sum=sum+b[j]
    else:
        sum=sum+a[i]
    i=i+1
print(sum)







            


