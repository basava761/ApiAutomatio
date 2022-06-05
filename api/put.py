import requests
import json
import jsonpath

url = 'https://reqres.in/api/users/2'
file = open("C:\\Users\\basav\\Desktop\\json.txt", 'r')

json_input = file.read()

req_json = json.loads(json_input)

response = requests.put(url, req_json)

assert response.status_code == 200

response_json = json.loads(response.text)
print(response_json)
print('*****************************************************')
print(response)
print('*****************************************************')
print(response.headers)
print('*****************************************************')
print(response.headers.get('Content-Type'))
