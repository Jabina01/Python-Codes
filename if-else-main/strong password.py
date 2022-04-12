alphabet=(input("enter the aphabet :"))
special_charector=(input("enter the charector :"))
number=int(input("enter the number : "))
if alphabet>="a"or alphabet<="z" and alphabet>="A" or alphabet<="Z":
    print("alphabet")
    if special_charector=="@" or special_charector=="#":
        print("special charector")
        if number>=1:
            print("number")
        else:
            print("no number")
    else:
        print("nospecial charector")
else:
    print("no alphabet")                            