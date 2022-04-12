passmarks=80
distinctionpassmarks=90
userscore=float(input("please enter your score"))
if userscore>=passmarks:
    if userscore>=distinctionpassmarks:
        print("you got a distinction")
    else:
        print("you passed")
else:
    print("you did not pass")