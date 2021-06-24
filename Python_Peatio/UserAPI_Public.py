import hmac
import hashlib 
import binascii
import time
import json
import http.client
from Python_Peatio.Auth import Auth

class UserAPI_Public(Auth):

    def trading_fees(self, URL : str)  -> list:
        "Returns trading_fees table as paginated collection"
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/trading_fees")
        trading_fees = json.loads(conn.getresponse().read().decode("utf-8"))


        return trading_fees