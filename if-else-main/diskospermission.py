# permission 
# print("taking permission to go out")
disco=input("give us permission to go out")
if disco=="yes":
    print("you can go")
    time=int(input("what time is it"))
    if time<=2:
        print("you can go")
        mask=input("i have to wear mask?")
        if mask=="yes":
            print("great")
            friend=(input("you have to go with ur friend"))
            if friend=="no":
                print("not allowed")
            else:
                print("u r allowed to go")
        else:
            print("not good")
    else:
        print("not necessory")
else:
    print("why you have to go")