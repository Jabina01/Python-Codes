def pangram():
    string="the quick brown fox jumps over the lazy dog"
    alphabit="abcdefghijklmnopqrstuvwxyz"
    a=True
    for i in alphabit:
        if i not in string:
            a=False
    if(a==True):
        print("pangram")
    else:
        print("not pangram")
pangram()
