a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>b>c:
    print(a,"is greater")
elif b>c>a:
    print(b,"is greater")
elif c>a>b:
    print(c,"is greater")
else:
    print("invailed")