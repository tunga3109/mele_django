import requests
from config_cur import *
#from datetime import datetime
import time
import json

##milliseconds = int(round(time.time() * 1000))
##print(milliseconds)
#
#DEMO_URL = 'https://demo-api-adapter.backend.currency.com'
#
## date in string format
##now = '19.07.2022 12:55:46'
### convert to datetime instance
##date_time = datetime.strptime(now, '%d.%m.%Y %H:%M:%S')
##print(date_time)
#
## timestamp in milliseconds
##ts = date_time.timestamp() * 1000
##print(ts)
#
#response = requests.get(DEMO_URL + '/api/v1/time')
#print(response.json()['serverTime'])
#
#
#session = requests.Session()
#session.headers['X-MBX-APIKEY'] = API_KEY
#
#response = session.get(
#    DEMO_URL + '/api/v1/account',
#    params={
#        'timestamp': response.json()['serverTime'],
#        'signature': 'a4b7e86ecab58df131f5bc7e96049b9ae9be35936400c0bc664079886febafae'}
#        )
#
#print(response.json())


import hmac
import hashlib

secret_key = bytes(secret_key,encoding='utf-8')
session = requests.Session()

URL = "account"
timestamp = int(time.time() * 1000)
recvWindow = "5000"
params = "timestamp=" + str(timestamp) + "&recvWindow=" + recvWindow
sign = hmac.new(secret_key, params.encode('utf-8'), hashlib.sha256).hexdigest()
params = params + "&signature=" + sign

response = session.get(
    'https://demo-api-adapter.backend.currency.com/api/v1/' + URL + '?' + params,
    headers={'X-MBX-APIKEY': API_KEY }

    )
data = json.loads(response.text)
print(data)
