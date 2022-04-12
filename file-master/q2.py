file = open("people1-exercise","r") 
Counter = 0
Content = file.read() 
CoList = Content.split("\n") 
for i in CoList: 
    Counter += 1
print("This is the number of lines in the file") 
print(Counter) 