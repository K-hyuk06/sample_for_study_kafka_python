import requests
from random import randint
import json
import time


headers = {'Content-Type': 'application/json; charset=utf-8'}

# requests.post(url="http://127.0.0.1:5000/api/status",headers=headers,data=json.dumps(example1))

while True:
    # time.sleep(30)
    floor=randint(1,9)
    number=randint(1,9)
    room_number=f"{floor*100+number}"
    
    
    example={'name':"room"+room_number,"checkout":True}


    
    requests.post(url="http://127.0.0.1:5000/api/checkout",headers=headers,data=json.dumps(example))
    time.sleep(30)
# print(example1,example2)