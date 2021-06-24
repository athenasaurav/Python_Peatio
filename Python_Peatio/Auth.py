import hmac
import hashlib 
import binascii
import time


class Auth:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def signed_param(self):
        nonce = int(time.time() * 1000)
        byte_key = bytes(self.secret_key, 'UTF-8')
        message = (str(nonce) + self.access_key).encode()
        signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        headers = {
        'X-Auth-Apikey': self.access_key,
        'X-Auth-Nonce': nonce,
        'X-Auth-Signature': signature
        }
        return nonce, signature

    def header(self):
        nonce = int(time.time() * 1000)
        byte_key = bytes(self.secret_key, 'UTF-8')
        message = (str(nonce) + self.access_key).encode()
        signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        header = {
        'X-Auth-Apikey': self.access_key,
        'X-Auth-Nonce': nonce,
        'X-Auth-Signature': signature
        }
        return header