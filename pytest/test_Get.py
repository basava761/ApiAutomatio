import requests
import json

from requests import Response

from payload import payload


url = "https://reqres.in/api/users?page=2"


def test_get():
    r = requests.get(url)
    print(r.status_code)
    print(r.content)
    json_r = r.text
    print(json_r)
    assert r.status_code==200




url2="https://reqres.in/api/users"
def test_post():
    res=requests.get(url2,json=payload())
    print(res.status_code)
    print(res.content)
    print(res.headers)