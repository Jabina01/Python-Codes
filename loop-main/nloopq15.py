height=int(input("Please enter height : "))
row=1
#top half of diamond
while(row<height+1):
    spaces=0
    while (spaces<(height-row)):
        spaces+=1
        print ("",end='')

    j=2*row-1
    while (j>0):
        j=j-1
        print("*",end='')
    row+=1
    print()

row=height-1
#bottom half of diamond
while (row>0):
    spaces=0
    while(spaces<height-row):
        spaces+=1
        print("",end='')
    j=2*row-1
    while(j>0):
        print("*",end='')
        j=j-1
    row=row-1
    print()