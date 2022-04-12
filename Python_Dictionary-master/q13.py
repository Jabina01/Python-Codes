from collections import Counter
 
# Initial Dictionary
my_dict ={

    'a':50, 

    'b':58, 

    'c':56,

    'd':40, 

    'e':100, 

    'f':20

    }
k = Counter(my_dict)
high = k.most_common(3)
print("Dictionary with 3 highest values :")
print("keys")
 
for i in high:
    print(i[0],",",end=" ")
