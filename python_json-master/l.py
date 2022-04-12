import json
import re
print("welcome to login and sign up page")
user=input("what u want to do login or sign up:")
# dic={}
if user=="signup":
    user_name=input("enter the user_name ")
    password1=input("enter ur password")
    password2=input("confirm ur password")
    
    if password1==password2:
        # print("ur password is strong")
        description=input("enter ur descriptinon")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        dob=input("enter ur dob")
        hobbies=input("enter ur hobbies")
        gender=input("enter ur gender f/m ")
        print("congrates",user,"u r sucessfully signupped")
        user_details={"user_name":user_name,"password2":password2,"description":description,"dob":dob,"hobbies":hobbies,"gender":gender}
        # dic.update({password2:user_details})
        with open("user.json","w")as file :
            a=json.dump(user_details, file,indent=2)
            print(a) 
    # else:
    #     print("weak password")
    else:
        print("Passwords didn't match.")                                                                                                                                    
elif user=="login":
    name=input("enter the usee_name")
    password=input("enter the password")
    with open("user.json","r")as file :
        data=json.load(file)
        if password==data["password2"]:
            print("congrates",name,"u have logged sucessfully")
            print("ur information is correct")
            print(data)
    
else:
    print("You have not signed up.Please signup before logging in.")
        