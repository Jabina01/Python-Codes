i=0
while i<5:
    j=0
    while j<5:
        if i==0 or j==0 or i==4 or j==4:
            print('a',end=' ')
        elif i==j==2:
            print('c',end=' ')
        else:
            print('b',end=' ')
        j=j+1
    print()
    i=i+1