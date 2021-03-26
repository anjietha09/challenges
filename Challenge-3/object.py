import json
import ast

# Get the value of an object which is in dict format
def output(data,path):
    for key in path.split("/"):
        if isinstance(data, (list, tuple)):
           val = data[int(key)]
        else:
          if key in data:
            val = data[key]
          else:
            val = None
            break
        data = val
    if val is None or val == '':
        return default
    else:
        return val

# Input for dict object like {"a":{"b":{"c":"d"}}}

dict_obj=input("Enter the object")
d = ast.literal_eval(dict_obj)

# Input for Key like a/b/c

key=input("Enter the key")
print(output(d,key))