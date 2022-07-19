import requests
from config_cur import *
from datetime import datetime
import time
  
# ts stores the time in seconds
ts = time.time()
  
# print the current timestamp
print(ts * 1000)

DEMO_URL = 'https://demo-api-adapter.backend.currency.com'

# date in string format
#now = '19.07.2022 12:55:46'
## convert to datetime instance
#date_time = datetime.strptime(now, '%d.%m.%Y %H:%M:%S')
#print(date_time)

# timestamp in milliseconds
#ts = date_time.timestamp() * 1000
#print(ts)

response = requests.get(DEMO_URL + '/api/v1/time')
print(type(response.json()['serverTime']))

response = requests.get(
    DEMO_URL + '/api/v1/account',
    headers={'X-MBX-APIKEY': API_KEY},
    params={
        'timestamp': response.json()['serverTime'],
        'signature': '91a1844732201ac7900dd490e15b27b2a5338b0a2293fbb3ef468b8e2ec3f497'}
        )

print(response.json())


