import json

import requests

url = "https://reqres.in/api/users"

file = open("C:\\Users\\basav\\Desktop\\json.txt", 'r')

json_input = file.read()

req_json = json.loads(json_input)

response = requests.post(url, req_json)
print(response.headers.get('Content-Length'))
assert response.status_code == 201
print(response)