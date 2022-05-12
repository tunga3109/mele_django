import requests
from config import API_KEY, username, password
import sys
#from encrypted_pass import encryptPassword

URL = 'https://demo-api-capital.backend-capital.com' #base url


session = requests.Session()
session.headers['X-CAP-API-KEY'] = API_KEY

#Returns the user's session details and optionally tokens. endpoint - /api/v1/session

response = session.post(
    URL + '/api/v1/session',
    json={'identifier': username, 'password': password},
    headers={'VERSION': '2'}
)

session.headers['CST'] = response.headers['CST']
session.headers['X-SECURITY-TOKEN'] = response.headers['X-SECURITY-TOKEN']


print(response.json())
print(session.headers)


#def get_encryprion_key():
#    response = session.get(
#        URL + '/api/v1/session/encryptionKey',
#        headers={'X-CAP-API-KEY' : API_KEY}
#        )
#    
#    print(response.json()['encryptionKey'])
#    print(response.json()['timeStamp'])



def get_history_activity_by_dealId(dealID) -> str:
    response = session.get(
        URL + '/api/v1/history/activity',
        params = { "detailed": True, "filter":"type==POSITION", "dealId": dealID, 'from': '2022-04-25T00:00:00.000' , 'to': '2022-05-10T00:00:00.000'}, 
        headers={'CST': session.headers['CST'], 'X-SECURITY-TOKEN': session.headers['X-SECURITY-TOKEN']}   
    )

    print(response.json())


#def get_preferences():
#    response = session.get(
#        URL + '/api/v1/accounts/preferences',
#        headers={'CST': session.headers['CST'], 'X-SECURITY-TOKEN': session.headers['X-SECURITY-TOKEN']} 
#    )
#
#    print(response.json())

    
#get_encryprion_key()
#get_history_activity_by_dealId('0015421d-0055-311e-0000-000080a5744c')

# encrypt password
#print(encryptPassword('MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuV20KiQJJf2uFsKAL2nxBvZb5JFD20Q3zCqVN7cbQVl2nyc7jBGkxQBLaNxRIh1RHgSSCCCwPb+InSdfu5pTLo4wsMmru/F6Mhg2x9Zmz39fmd7xqZ3bCIjPRgpEWZWkTkYW2y9Rk8nJfAZS+yqmpmfi8BXpDDnSZX0vmDQXweR0Wl+k9AYTs2p8qamFpMM50Cm4Rm9xuZaIOyQqnjhwoF9jdKRJWCmdX4WfbjFjr1KB6q5QCDIlfH49gh+DPlkc7zSwaZw5X/lDokJBSzNZ87HMiRQK5WQiYoc8RSEoH1xNf+laG5CyX1iL3Pq15HKfGmXqqm3z1+UmvjFfdZZDsQIDAQAB',password,'1651395793516'))

#get_preferences()












    