import json
Dic={
    "name": "David",
     "class":"I",
     "age": 6 
    }
# out_file = open("yourfile.json", "w")
# json.dump(Dic, out_file, indent = 6)
# out_file.close()

mystring=json.dumps(Dic,indent=1)
print(mystring)