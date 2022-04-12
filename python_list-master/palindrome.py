
name=['n','k','t','k','n']

i=1
a=[]
while i<=len(name):
    a.append(name[-i])
    i=i+1
if (name==a):
    print("palindrome")
else:
    print("not palindrome")