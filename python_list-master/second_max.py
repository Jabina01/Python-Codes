numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
a=numbers[i]
while i<len(numbers):
    if numbers[i]>a:
        a=numbers[i]
    i=i+1
numbers.remove(a)
i=0
l=numbers[i]
while i<len(numbers):
    if numbers[i]>l:
        l=numbers[i]
    i=i+1
print(l)




