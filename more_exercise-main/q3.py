# import re
# def uppercase_check(password):
#     if re.search('[A-Z]', password): #atleast one uppercase character
#         return True
#     return False

# def lowercase_check(password):
#     if re.search('[a-z]', password): #atleast one lowercase character
#         return True
#     return False

# def digit_check(password):
#     if re.search('[0-9]', password): #atleast one digit
#         return True
#     return False

# def special_char(password):
#     if re.search('[#,$,%,&,@]', password): 
#         return True
#     return False

# def user_input_password_check():
#     password = input("Enter password : ")
#         #atleast 8 character long
#     if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password) and  special_char(password): 

#         print("Strong Password")
#     else:
#         print("Weak Password")
# user_input_password_check()


        
import re
# def uppercase_check(password):
if re.search('[A-Z]') and re.search('[a-z]') and re.search('[0-9]' and  re.search('[#,$,%,&,@]'
#     return True
# return False

# def lowercase_check(password):
if re.search('[a-z]') 
#     return True
# return False

# def digit_check(password):
if re.search('[0-9]', password): 
    return True
return False

# def special_char(password):
if re.search('[#,$,%,&,@]', password): 
    return True
return False

# def user_input_password_check():
password = input("Enter password : ")
if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password) and  special_char(password): 
    print("Strong Password")
else:
    print("Weak Password")
# user_input_password_check()














# string_name = "Shakrudin"

# print (len(string_name))







# string_name = "Rishabh Verma"

# print (len(string_name))






# string_name = "navgurukul"

# if "n" in string_name:

#     print ("n hai")

# else:

#     print ("n nahi hai")






#     print ("n" in string_name)

# print (type("n" in string_name))



