import requests
import json

#initialization of global variable
metadata_server = "http://169.254.169.254/latest/"
path_dict = {"meta-data/" : ''}
temp_dict = {}

# function returns a key and a list of values from instance metadata server
def get_info(key, url):
    values = requests.get(url).text
    path_list = [x for x in values.splitlines()]
    prt_key = key
    return prt_key, path_list
def get_metadata(path_list, url):
    for p in path_list:
        if p[-1] != '/':
           api_call = get_info(p, url+p)
           update(path_dict, api_call[0], api_call[1])
        else:
           api_call = get_info(p, url+p)
           temp_dict = { k:[] for k in api_call[1]}
           update(path_dict, api_call[0], temp_dict)
           get_metadata(api_call[1], url+api_call[0])
    return

# function finds a key in nested dictionary and will update its value
def update(dicts, key, value):
    for k,v in dicts.items():
        if k == key:
            dicts[k] = value
        elif isinstance(v, dict):
            update(dicts.get(k), key, value)
        elif not k in dicts.keys():
            dicts.update({ key : value })
    return

# initialize path_list and calling met_gen function
path_list = ["meta-data/"]
get_metadata(path_list, metadata_server)

# json object
json_data = json.dumps(path_dict, indent=4)
print(json_data)
