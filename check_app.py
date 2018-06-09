import requests
import json
import time

time.sleep(5)

r = requests.post('http://127.0.0.1:5000/command/send',
                  data=json.dumps({'address': 0, 'sub_address': 0,
                                   'packet': [0x1234]+[-1]*29+[0, 0]}),
                  headers={'Content-Type': 'application/json'})
print(r.text)