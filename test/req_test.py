import requests
import time
import json

url = 'http://127.0.0.1:5000/login'

header = {'content-type':'application/json'}
form = {'name':'zonya'}

r = requests.post(url,data=json.dumps(form),headers=header)

print(r.status_code)
print(r.text)

url_get = 'http://127.0.0.1:5000/login?name=zonya'
r = requests.get(url_get)
print(r.status_code)
print(r.text)