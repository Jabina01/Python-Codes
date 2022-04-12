question_list=["What is the capital of India"]
option_list=["Chandigarh","Bhopal","Chennai","Delhi"]
solution_list = [1,2,3,4]
answer_list=["Chandigarh","Bhopal","Chennai","Delhi"]
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    while j<len(option_list):
        print(k,".",option_list[j])
        k=k+1
        j+=1
    i=i+1

 
# i=0
# user=input("enter the answer")
# question_list=["What is the capital of India"]
# question_list=len(question_list)
# index=0
# while index<question_list:
#     print(question_list)
#     index=index+1
# i=i+1