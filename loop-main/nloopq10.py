i=0
while i<5:
    print(' '*(4-i),end=' ')
    j=0
    while j-1<i*2:
        if (j+1)>(i+1):
            print(chr(65+(i*2)-j),end=' ')
        else:
            print(chr(65+j),end=' ')
        j=j+1
    print()
    i=i+1


# i=0
# while i<5:
#     print(' '*(4-i),end=' ')
#     j=0
#     while j-1<i*2:
#         if (j+1)>(i+1):
#             print(chr(65+(i*2)-j),end=' ')
#         j=j+1
#     print()
#     i=i+1

