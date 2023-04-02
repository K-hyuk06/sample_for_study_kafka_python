import requests
from random import randint
import json
import time
data = []


headers = {'Content-Type': 'application/json; charset=utf-8'}

# requests.post(url="http://127.0.0.1:5000/api/status",headers=headers,data=json.dumps(example1))

while True:
    example1={'name':"room101","temp":30.2+randint(-10,10)}
    example2={'name':"room102","temp":10.2+randint(-10,10)}

    time.sleep(1)
    requests.post(url="http://127.0.0.1:5000/api/status",headers=headers,data=json.dumps(example1))
    requests.post(url="http://127.0.0.1:5000/api/status",headers=headers,data=json.dumps(example2))
# print(example1,example2)