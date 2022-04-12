list1 = [1, 5, 10, 12, 16, 20]

list2 = [1, 2, 10, 13, 16]
a=[]
i=0
while i<len(list1):
    c=list1[i]
    if c not in a:
        a.append(c)
        a.sort()
        j=0
        while j<len(list2):
            b=list2[j]
            if b not in a:
                a.append(b)
                a.sort()
            j=j+1
    i=i+1
print(a)
