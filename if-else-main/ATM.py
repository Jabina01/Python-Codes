print("wellcome to the ATM")
ATM=(input("insert your atm"))
if ATM:
    print("please wait for the process")
    language=input("select your language")
    if language=="english"or"hindi":
        print("proceed")
        password=int(input("please enter your atm pin"))
        a= 9858
        if password==a:
            print("please wait.. we are chacking the password")
            a=input("choose your account")
            if a=="saving"or"reserve":
                print("to be continue with saving account")
                cash=(input("select transaction option"))
                if cash== "withdraw":
                    print("proceeding")
                    money =int(input("enter the ammount"))
                    if money>99 and money<10001:                
                        print("please wait transaction is proceeding")
                    else:                        
                        print("please  collect your cash")
                        print("somthing is wrong")
                else:
                    print("transaction recipt")
            else:
                print("to be continue with curunt account")
        else:
            print("wrong password")
    else:
        print("हिंदी जारी रखें")
else:
    print("card is not properly inserted please try again")

