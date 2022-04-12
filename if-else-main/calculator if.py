number=int(input("enter a number"))
number1=int(input("enter another number"))
oprt=input("enter the opration symbol which you want")
if number>=1 and number1>=1:
    if oprt=="+":
     print(number + number1)
    elif oprt=="-":
        print(number-number1)
    elif oprt=="*":
        print(number*number1)
    elif oprt=="/":
        print(number/number1)
    elif oprt=="//":
        print(number//number1)
    elif oprt=="%":
        print(number%number1)
    elif oprt=="**":
        print(number**number1)
    else:
        print("unknown opration")
else:
    print("error")
                      