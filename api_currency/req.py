import requests
from config_cur import *
from datetime import datetime

DEMO_URL = 'https://demo-api-adapter.backend.currency.com'

# date in string format
now = '19.07.2022 12:55:46'
# convert to datetime instance
date_time = datetime.strptime(now, '%d.%m.%Y %H:%M:%S')
print(date_time)

# timestamp in milliseconds
ts = date_time.timestamp() * 1000
print(ts)

response = requests.get(DEMO_URL + '/api/v1/time')
print(response.text)


