import requests
from config import API_KEY, username, password
import sys
import json
#from encrypted_pass import encryptPassword

URL = 'https://demo-api-capital.backend-capital.com' #base url
        
# Create session
session = requests.Session()

# Returns the user's session details and optionally tokens.
response = session.post(
    URL + '/api/v1/session',
    json={'identifier': username, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)
#session.headers['CST'] = response.headers['CST']
#session.headers['X-SECURITY-TOKEN'] = response.headers['X-SECURITY-TOKEN']

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

#print(response.status_code)
#print(response.json())


class API:
    '''
    CAPITAL.COM TRADING API
    '''
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_encryprion_key(self):
        response = session.get(
            URL + '/api/v1/session/encryptionKey',
            headers={'X-CAP-API-KEY' : self.api_key}
            )

        #print(response.json()['encryptionKey'])
        #print(response.json()['timeStamp'])

    def get_history_activity_by_dealId(self, dealID, filter, per_from, per_to) -> str:
        response = session.get(
            URL + '/api/v1/history/activity',
            params = { "detailed": True, "filter": filter, "dealId": dealID, 'from': per_from , 'to': per_to},
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}     
        )

        print(response.json())

    def get_preferences(self):
        response = session.get(
            URL + '/api/v1/accounts/preferences',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
        )
    
        print(response.json())







api_test = API(API_KEY)
#api_test.get_encryprion_key()
#api_test.get_history_activity_by_dealId('0015421d-0055-311e-0000-000080a5744c', "type==POSITION", '2022-04-25T00:00:00.000', '2022-05-12T00:00:00.000')
#api_test.get_preferences()


#with open('api_trading.json', 'w') as file:
#    json.dumps(api_test.get_history_activity_by_dealId('0015421d-0055-311e-0000-000080a5744c', "type==POSITION", '2022-04-25T00:00:00.000', '2022-05-12T00:00:00.000'))





    















    