name="jabeena"
count=0
d={}
for i in name:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
