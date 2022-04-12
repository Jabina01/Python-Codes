i=0
sum=0
avg=0
while i<11:
    num=int(input("enter the weight:"))
    sum=sum+num
    avg=sum/11
    i=i+1
print("Average of weight",avg)
print("Sum is ",sum)
if avg%5==0:
    print("divisible 5")
else:
    print("Not divisible by 5")
   