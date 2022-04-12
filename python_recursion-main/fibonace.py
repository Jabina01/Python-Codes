# def fib(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return fib(number-1) + fib(number-2)

# def getFibList(number):
#     fib_list = []
#     key = 1
#     while (key < number + 1):
#         fib_list.append(fib(key))
#         key += 1
#     return fib_list

# print(getFibList(10))




def fibonacci(i):
   if i ==0:
      return 0
   elif i==1:
      return 1
   else:
      return fibonacci(i-2)+fibonacci(i-1)
for x in range (10):
   print(fibonacci(x))
