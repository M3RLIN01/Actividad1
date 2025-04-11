import json

json_file = []
with open('myfile.json', 'r') as file:
    ourjson =json.load(file)

for i in ourjson['tokens']:
    print(i['token'])
    print(i['expiry_time'])