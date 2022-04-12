# def max_function():
#     a=[]
#     b=3
#     for i in range(b):
#         n=int(input("enter the number"))
#         a.append(n)
#     max=a[0]
#     for i in range(b):
#         if (a[i]>max):
#             max=a[i]
#     print(max)
# max_function()

quantity =int (input("enter quantity"))
if quantity*100>1000:
    print(quantity*100-(.1*quantity*100))
else:
    print(quantity*100)