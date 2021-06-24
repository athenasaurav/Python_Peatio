import hmac
import hashlib 
import binascii
import time
import json
import http.client
from Python_Peatio.Auth import Auth

class Market(Auth):

    def trades(self, URL : str, limit = 1, page = 1, order_by = 'desc')  -> dict:
        "Get your executed trades. Trades are sorted in reverse creation order."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/tickers?limit={limit}&page={page}&order_by={order_by}".format(limit= limit, page = page, order_by= order_by))
        trades = json.loads(conn.getresponse().read().decode("utf-8"))

        return trades
    
    

    def all_cancel_custom(self, URL : str, side, market)  -> dict:
        "Cancel all my orders custom. If only asks order to cancel pass asks, if only asks order of btc usdt need to be cancelled then pass btcusdt"
        cancel_payload = "{\r\n \"side\" : \"%s\", \r\n \"market\" : \"%s\"\r\n}"% (side, market)
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("POST", "/api/v2/peatio/market/orders/cancel", cancel_payload, header)
        all_cancel_custom = json.loads(conn.getresponse().read().decode("utf-8"))

        return all_cancel_custom

    def all_cancel(self, URL : str)  -> dict:
        "Cancel all my orders. Bids & Asks all cancelled of all market"
        cancel_payload = "{}"
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("POST", "/api/v2/peatio/market/orders/cancel", cancel_payload, header)
        all_cancel = json.loads(conn.getresponse().read().decode("utf-8"))

        return all_cancel

    def id_cancel(self, URL : str, id : int)  -> dict:
        "Cancel an order by order id."
        cancel_payload = "{}"
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("POST", "/api/v2/peatio/market/orders/{id}/cancel".format(id = id), cancel_payload, header)
        id_cancel = json.loads(conn.getresponse().read().decode("utf-8"))

        return id_cancel

    def create_limit_order(self, URL : str, market : str, side : str, volume : str, price : str )  -> dict:
        "Create a Sell/Buy order."
        payload = "{\r\n    \"market\": \"%s\",\r\n    \"side\" : \"%s\", \r\n    \"volume\" : \"%s\", \r\n    \"ord_type\" : \"limit\",\r\n    \"price\" : \"%s\"\r\n}"% (market, side, volume, price)
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("POST", "/api/v2/peatio/market/orders", payload, header)
        new_limit_order = json.loads(conn.getresponse().read().decode("utf-8"))

        return new_limit_order


    def get_order(self, URL : str, limit = 100, page = 1, order_by = 'desc', ord_type = 'limit')  -> dict:
        "Get your orders, result is paginated."
        payload = {}
        header = Auth.header(self)
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/market/orders?limit={}&page={}&ordering={}&ord_type={}".format(limit, page, order_by, ord_type), payload, header)
        orders = json.loads(conn.getresponse().read().decode("utf-8"))

        return orders