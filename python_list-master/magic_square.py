magic_square = [

    [8, 3, 4],

    [1, 5, 9],

    [6, 7, 2]

]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        sum=sum+magic_square[i][j]
        j=j+1
    i=i+1
print(sum)

d=0
while d<len(magic_square):
    j=0
    sum1=0
    while j<len(magic_square[d]):
        sum1=sum1+magic_square[d][j]
        j=j+1
    d=d+1
print(sum1)


c=0
b=0
sum3=0
while c<len(magic_square):
    sum3=sum3+magic_square[c][b]
    c=c+1
print(sum3)
    
