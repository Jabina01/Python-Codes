def calculator(number1,number2,operator):
    if operator =="+":
        return number1+number2
    elif operator=="-":
        return number1-number2
    elif operator=="*":
        return number1*number2
    elif operator=="/":
        return number1/number2
a=int(input("enter the ist number"))
b=int(input("enter the second number"))
o=input("enter the  operator")
n=calculator(a,b,o)
print(n)




# def list_change(a,b):
#     i=0
#     multiplly=0
#     while i<len(a):
#         multiply=a[i]*b[i]
#         print(multiply)
#         i=i+1
# list_change([5, 10, 50, 20], [2, 20, 3, 5])
    
