marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78],

    [87, 67, 49, 68, 88]
]
i=0
sum=0
while i<len(marks):
    j=0
    a=0
    avg=0
    while j<len(marks[i]):
        a=a+marks[i][j]
        j=j+1
    sum=sum+a
    i=i+1
    avg=sum/17
print(sum)
print(avg)