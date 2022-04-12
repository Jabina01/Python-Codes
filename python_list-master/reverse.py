# list=["jabu","naina","kushboo","mehak","ruhi"]
# i=0
# a=[]
# while i<len(list):
#     a.append(list[i])
#     i=i+1
# print(a)


# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# places.reverse()
# print(places)



places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
a=[]
i=len(places)-1
while i>=0:
    a=a+[i]
    a.append(places[i])
    i=i-1
print(a)


