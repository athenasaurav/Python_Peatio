===================================================
Welcome to Open Source Peatio Deployed Exchange API
===================================================

Updated 25th June 2021

.. image:: https://img.shields.io/pypi/l/python-binance.svg
    :target: https://pypi.org/project/Python-Peatio/
              
.. image:: https://img.shields.io/travis/sammchardy/python-binance.svg
    :target: https://pypi.org/project/Python-Peatio/

.. image:: https://img.shields.io/pypi/wheel/python-binance.svg
    :target: https://pypi.org/project/Python-Peatio/

.. image:: https://img.shields.io/pypi/pyversions/python-binance.svg
    :target: https://pypi.org/project/Python-Peatio/


This is an unofficial Python wrapper for the `Peatio exchange REST APIv2 <https://www.openware.com/sdk/2.3/docs/peatio/api/peatio-user-api-v2.html>`_. I am in no way affiliated with Peatio or Openware, use at your own risk.

If you came here looking for an exchange to purchase cryptocurrencies, then go `here <https://www.binance.com/en>`_ 


Source code
  https://github.com/athenasaurav/Python_Peatio

Features
--------

-  Implementation of all General, Market Data and Account endpoints.
-  Simple handling of authentication
-  No need to generate timestamps yourself, the wrapper does it for you
-  Response exception handling
-  Symbol Depth Cache
-  Kline/Candle fetching function
-  Withdraw functionality
-  Deposit addresses
-  API Trading

Quick Start
===========

Register an account with a Peatio Exchange.

Generate an API Key and API Secret.

Install
=======

::

    pip install Python_Peatio

To get Auth Parameter
=====================

::

    from Python_Peatio.Auth import Auth
    auth = Auth(api_key, api_secret)

To get Nonce and Signature
==========================
::

    auth.signed_param()

To get account balance of all the currency on exchange
======================================================
::

    from Python_Peatio.Accounts import Accounts
    Accounts = Accounts(api_key, api_secret)
    balances = Accounts.all_currency_balance(
        URL='your http peatio url')

To place an BUY order
=====================
::

    from Python_Peatio.Market import Market
    Market = Market(api_key, api_secret)
    order = Market.create_limit_order(
        URL='your http peatio url',
        market = 'symbol of cryptocurrency pair',
        side='buy',
        volume='0.002',
        price='38000')

To place an SELL order
======================
::
    
    from Python_Peatio.Market import Market
    Market = Market(api_key, api_secret)
    order = Market.create_limit_order(
        URL='your http peatio url',
        market = 'symbol of cryptocurrency pair',
        side='Sell',
        volume='0.002',
        price='38000')

To cancel an Buy or Sell order
==============================
::    
    
    from Python_Peatio.Market import Market
    Market = Market(api_key, api_secret)
    order = Market.id_cancel(
        URL='your http peatio url',
        id = buy or sell id to cancel)

All the use cases will be uploaded soon
---------------------------------------

