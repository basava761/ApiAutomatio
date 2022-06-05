import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)
# print(response.content)
print("headersare below")
print(response.headers)

pages = json_response = json.loads(response.text)
print(json_response)


pages = jsonpath.jsonpath(response,'total_pages')
print(pages[1])
