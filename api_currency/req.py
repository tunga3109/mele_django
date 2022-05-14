from urllib import response
import requests
from config import API_KEY, username, password

URL = 'https://api-adapter.backend.currency.com/'

session = requests.Session()
session.headers['X-MBX-APIKEY'] = API_KEY

#response = session.get(
#    URL + '/api/v1/account',
#)
#
#print(response.status_code)

