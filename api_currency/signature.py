import hmac
import hashlib

secret_key = b"n:ywt2A%=WfuBZ!0c&ilATmo0:B12YMI"
total_params = b"/api/v1/account/recvWindow=5000&timestamp=1658227449583&X-MBX-APIKEY=pH4GbKW3j5l2NTB9"
signature = hmac.new(secret_key, total_params, hashlib.sha256).hexdigest()
print("signature = {0}".format(signature))
