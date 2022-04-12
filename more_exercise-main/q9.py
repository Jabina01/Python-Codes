# def is_harshad_number():
#     num=int(input("enter any number"))
#     rem=sum=0
#     n=num
#     while(num>0):
#         rem=num%10
#         sum=sum+rem
#         num=num//10
#     if(n%sum==0):
#         print("true")
#     else:
#         print ("false")

# is_harshad_number()





def is_harshad_number(number):
  remainder = 0
  digit_sum = 0
  check = False
  n = number
  while(n > 0):
    remainder = n % 10
    digit_sum = digit_sum + remainder
    n = n//10
  if number % digit_sum == 0:
    check = True
  return check
lower = int(input("ENTER LOWEST NUMBER : "))
upper = int(input("ENTER HIGHEST NUMBER : "))
print("HARSHAD NUMBERS WITHIN RANGE ARE ".format(lower,upper))
for i in range(lower,upper+1):
  if is_harshad_number(i):
    print(i)





    




    