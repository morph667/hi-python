import json, os

file = "./ex00_json2ini/sample.json"

if(os.path.exists(file)):
    with open(file,'r') as file:
        file = json.loads(file.read())
        print(file)
else:
    print("file doesn't exist")