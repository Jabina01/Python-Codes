153
num=int(input("enter 3 digits number"))
temp=num
digit=0
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")




#print armstrong number from 1 to 100

# i=1
# sum=1
# digit=0
# while i<=100:
#     digit=i%sum==0
#     sum=sum+i*3
#     i=i//10    
# i=i+1
# if i%10==0:
#     print("it is an armstrong number") 
# else:
#     print("it is not an armstrong number")

