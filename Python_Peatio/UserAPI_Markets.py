import hmac
import hashlib 
import binascii
import time
import http.client
import json
from Python_Peatio.Auth import Auth

class UserAPI_Markets(Auth):

    def all_markets_tickers(self, URL : str)  -> dict:
        "Get ticker of all markets"
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/tickers")
        all_tickers = json.loads(conn.getresponse().read().decode("utf-8"))

        return all_tickers

    def market_tickers(self, market : str, URL : str)  -> dict:
        "Get ticker of specific market."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/{}/tickers".format(market))
        market_tickers = json.loads(conn.getresponse().read().decode("utf-8"))

        return market_tickers
    
    def markets_tickers_klines(self, market : str, URL : str , period = 1, limit = 30) -> dict:
        "Get OHLC(k line) of specific market."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/{}/k-line?period={}&limit={}".format(market, period, limit))
        klines = json.loads(conn.getresponse().read().decode("utf-8"))

        return klines
    
    def markets_tickers_depth(self, market : str, URL : str, limit = 300) -> dict:
        "Get depth or specified market. Both asks and bids are sorted from highest price to lowest."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/{}/depth?limit={}".format(market, limit))
        depth = json.loads(conn.getresponse().read().decode("utf-8"))

        return depth

    def markets_tickers_trades(self, market : str, URL : str, limit = 100, order_by = 'desc') -> dict:
        "Get recent trades on market, each trade is included only once. Trades are sorted in reverse creation order."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/{}/trades?limit={}&order_by={}".format(market, limit, order_by))
        trades = json.loads(conn.getresponse().read().decode("utf-8"))

        return trades

    def markets_tickers_order_book(self, market : str, URL : str, asks_limit = 10, bids_limit =10) -> dict:
        "Get the order book of specified market."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets/{}/order-book?asks_limit={}&bids_limit={}".format(market, asks_limit, bids_limit))
        order_book = json.loads(conn.getresponse().read().decode("utf-8"))

        return order_book

    def all_markets(self, URL : str, limit = 100, page = 1, ordering = 'asc') -> dict:
        "Get all available markets."
        conn = http.client.HTTPConnection(URL)
        conn.request("GET", "/api/v2/peatio/public/markets?limit={}&page={}&ordering={}".format(limit, page, ordering))
        all_markets = json.loads(conn.getresponse().read().decode("utf-8"))

        return all_markets

