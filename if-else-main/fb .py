#facebook
fb=input("do you want to create new account")
if fb=="no":
    print("log in")
    number=int(input("enter your number or email address"))
    if number>=9999999999 or number<=9999999999:
        print("connecting")
        password=input("enter your password")
        if password=="a1b2c3d4":
           print("you are logged in")
        else:
           print ("wrong password")
    else:
        print("invailed connection")
else:
    print("create new account")