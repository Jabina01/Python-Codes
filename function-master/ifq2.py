# def perfect(num):
#     sum=0
#     i=1
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#         i=i+1
#     if num==sum:
#         print(num,"is a perfect number")
#     else:
#         print(num,"is not a perfect number")
# perfect(6)




MinValue = int(input("Enter any Minimum Value: "))
MaxValue = int(input("Enter any Maximum Value: "))
for Number in range(MinValue, MaxValue - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n
    if(Sum == Number):
        print(Number)





