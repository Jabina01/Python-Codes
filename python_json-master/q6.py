import json
python_obj='{"a":  1,"a":  3,"a":  3, "a": 4,"b": 1,"b": 2 }' 
json_obj=json.loads(python_obj)
print("unique key in a json object:")
print(json_obj)
