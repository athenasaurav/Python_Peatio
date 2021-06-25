import hmac
import hashlib 
import binascii
import time
import http.client
from Python_Peatio.Auth import Auth

class Accounts(Auth):

    def account_balances_currency(self, URL : str, currency : str)  -> dict:
        "Get list of user accounts balances of selected currency"
        payload = {}
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/account/balances/{currency}".format(currency = currency), payload, header)
        currency_balance = json.loads(conn.getresponse().read().decode("utf-8"))

        return currency_balance


    def all_currency_balance(self, URL : str)  -> list:
        "Get list of user accounts balances of all currency"
        payload = {}
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/account/balances", payload, header)
        all_currency_balance = json.loads(conn.getresponse().read().decode("utf-8"))

        return all_currency_balance
