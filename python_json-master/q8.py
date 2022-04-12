import json
list1=["neelam","programer","24","2400",]
keys1=["name","desination","age","salary"]
emp1={}
for keys in keys1:
    for values in list1:
        emp1[keys]=values
        list1.remove(values)
        break
list2=["komal","trainer","25","2000",] 
keys1={"name","desination","age","salary"}
emp2={}
for keys in keys1:
    for values in list2:
        emp2[keys]=values
        list2.remove(values)
        break 
list3=["abishek","manager","29","63000",] 
keys1={"name","desination","age","salary"}
emp3={}
for keys in keys1:
    for values in list3:
        emp3[keys]=values
        list3.remove(values)
        break 
list4=["anuradha","HR","25","40000",] 
keys1={"name","desination","age","salary"}
emp4={}
for keys in keys1:
    for values in list4:
        emp4[keys]=values
        list4.remove(values)
        break 
dict1={}
dict1.update({"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4})
print(dict1)
with open("salary.json","w")as json_file:
    json.dump(dict1,json_file,indent=2)




# import json
# # a Python object (dict):
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# print(type(python_obj))
# # convert into JSON:
# j_data = json.dumps(python_obj)

# # result is a JSON string:
# print(j_data)