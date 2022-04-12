test_list =  [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]

 
# printing original list
print("The original list : " +  str(test_list))
  
# Using set() + values() + dictionary comprehension
# Get Unique values from list of dictionary
res = list(set(val for dic in test_list for val in dic.values()))
      
# printing result 
print("The unique values in list are : " + str(res))
