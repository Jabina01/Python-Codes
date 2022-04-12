number=[50,40,23,22,24,33,70,56,12,5,10,7]
a=[]
i=0
k=number[0]
while i<len(number):
    if number[i]>20 and number[i]<40:
        j=number[i]
        a.append(j)
    i=i+1
print(a)