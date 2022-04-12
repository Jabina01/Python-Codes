f=open("people7.txt","r")
for i in f:
    if "delhi" in i:
        a=open("delhi.txt","a")
        a.write(i)
    elif "shimla" in i:
        b=open("shimla.txt","a")
        b.write(i)
    else:
        c=open("other.txt","a")
        c.write(i)