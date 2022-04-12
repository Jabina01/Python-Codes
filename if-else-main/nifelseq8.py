winning_number=55
user_guess=int(input("enter user_guess"))
if winning_number==user_guess:
    print("you win")
else:
    if user_guess<winning_number:
        print("you guessed too low")
    else:
        print("you guessed too high")

