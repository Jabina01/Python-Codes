winning_number=27
user_input=input ("guess a number between 1 and 100")
user_input=int(user_input)
if user_input==winning_number:
    print("you win!!!")
else:
    if user_input<winning_number:
        print("too low")
    else:
        print("too high")