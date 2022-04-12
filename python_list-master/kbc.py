question_list = ["How many continents are there?",  "What is the capital of India?",    "NG mei kaun se course padhaya jaata hai?"]


options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]

]


# har ek question ke liye, uski solution key (yeh index nahi hai)

solution_list = [3, 4, 1]
answer_list=[
    ["1.four","3.seven"],
    ["2.bhopal","4.delhi"],
    ["1.software engenering","4.agriculture"]

]
print("kaun banaga cororepati(kbc)")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    while j<len(options_list[i]):
        print(k,".",options_list[i][j])
        k=k+1
        j+=1
    num1=input("do u want 50 50 lifeline")
    if num1=="yes":
        print("50 50 life line")
        if count<1:
            print(answer_list[i])
            num2=int(input("enter ur answer"))
            if num2==solution_list[i]:
                s=+10000
                print("ur answer is correct")
                print("u win Rs/",s)
            else:
                print("ur answer is incorrect")
                break
            count+=1
        else:
            print("u already use lifeline")
            m=int(input("enter ur answer"))
            if m==solution_list[i]:
                print("congrates ur answer is right")
                s=+10000
                print("u win",s)
            else:
                print("ur answer is wrong")
                print("u can play again")
                print("u win",s)
                break
    else:
        k=int(input("enter ur answer"))
        if k==solution_list[i]:
            print("right answer")
            s+=10000
            print("u win Rs/",s)
            print("congress")
        else:
            print("no chance")
            print("ur answer is wrong")
            break
        
    i=i+1


            
