import json

import requests

url = "https://www.rahulshettyacademy.com/"

se = requests.session()
se.cookies.update({'visidate': 'february'})

cookies = {'visidate': 'february'}

r = se.get(url, )

print(r.status_code)

print(r.content)
print(r.text)
