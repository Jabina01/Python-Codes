height_limit=105
age_limit=8
height=int(input("enter your height in cm"))
age=int(input("enter your age in years"))
if height>=height_limit:
    if age>=age_limit:
        print("you may go on the ride")
    else:
        print("you are too young for this ride,sorry")
else:
    print("you can not go on this ride ,you are too short, sorry")