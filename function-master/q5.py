#check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"
# def check_numbers(num1,num2):

#     if num1 and num2%2==0:
        
#         return "dono even ha"
    
#     else:
        
#         return "dono numbers even nhi ha"

# print(check_numbers(5,7))





def check_numbers(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("even")
        elif a[i]%2==0 and b[i]%2!=0:
            print("odd even")
        else:    
            print("dono odd ha")
        i=i+1   
check_numbers(a=[2, 6, 18, 10, 3, 75] ,b= [6, 19, 24, 12, 3, 87])
    

