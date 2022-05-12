from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode

def encryptPassword(encrypted_key:str ,password:str ,timestamp:str):

    input = bytes(password + '|' + timestamp, encoding='UTF-8')
    input_1 = b64encode(input)

    key = b64decode(bytes(encrypted_key, encoding='UTF-8'))
    key = RSA.importKey(key)

    cipher = PKCS1_OAEP.new(key)
    ciphertext = b64encode(cipher.encrypt(input_1))



    return ciphertext

print(encryptPassword('MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuV20KiQJJf2uFsKAL2nxBvZb5JFD20Q3zCqVN7cbQVl2nyc7jBGkxQBLaNxRIh1RHgSSCCCwPb+InSdfu5pTLo4wsMmru/F6Mhg2x9Zmz39fmd7xqZ3bCIjPRgpEWZWkTkYW2y9Rk8nJfAZS+yqmpmfi8BXpDDnSZX0vmDQXweR0Wl+k9AYTs2p8qamFpMM50Cm4Rm9xuZaIOyQqnjhwoF9jdKRJWCmdX4WfbjFjr1KB6q5QCDIlfH49gh+DPlkc7zSwaZw5X/lDokJBSzNZ87HMiRQK5WQiYoc8RSEoH1xNf+laG5CyX1iL3Pq15HKfGmXqqm3z1+UmvjFfdZZDsQIDAQAB', 'Xuxin_1003199954321', '1651394551440'))









