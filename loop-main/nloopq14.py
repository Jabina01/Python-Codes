rows = int(input("Enter Inverted Pyramid Pattern Rows = "))

print("Inverted Pyramid Star Pattern") 

i = rows
while(i >= 1):
    j = 0
    while(j <= rows - i):
        print(end = ' ')
        j = j + 1
    k = 0
    while(k < i):
        print('*', end = ' ')
        k = k + 1
    i = i - 1
    print()