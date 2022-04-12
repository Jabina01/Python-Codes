string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
i=0
a=[]
while i<len(string_list):
    h=string_list[i]
    if h not in a:
        a.append(h)
    i=i+1
print(a)