import requests
from config_cur import *
import time
import json
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
