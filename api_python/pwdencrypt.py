from passwords import en_key, password, timestamp
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode,b64encode
import sys


input = password + '|' + timestamp


keyDER = b64decode(en_key)
keyPub = RSA.importKey(keyDER)
cipher = Cipher_PKCS1_v1_5.new(keyPub)
cipher_text = cipher.encrypt(input.encode())
emsg = b64encode(cipher_text)

print(emsg)







