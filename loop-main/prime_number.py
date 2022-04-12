# print('Prime numbers between 1 and 100 are:')
 
# for num in range(2,101):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)




num=int(input("enter number: "))
i=1
c=0
while i<=num:
    if num%i==0:
        c=c+1
    i=i+1
if c==2:
    print("Prime number.")
else:
    print("composite number.")
