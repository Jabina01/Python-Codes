def even_odd():
    elements = [1,2,3,4,5,6,7,8,9]
    i=0
    a=[]
    while i<len(elements):
        j=elements[i]
        if j%2==0:
            a.append(j)
        i=i+1 
    print("even numbers",a)
        
even_odd()