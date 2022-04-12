import json
data={"name":"seerat",
    "class":"ist",
    "age":5,
    "roll number":10} 
print(data)
print("JSON data:")
a=(json.dumps(data, sort_keys=True,indent=1))
print(a)
