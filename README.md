## Open Source Peatio Deployed Exchange API

This is an unofficial Python wrapper for the [Peatio exchange REST API v2](https://www.openware.com/sdk/2.3/docs/peatio/api/peatio-user-api-v2.html). I am in no way affiliated with Openware Peatio Project, use at your own risk.

If you came here looking for the exchange to purchase cryptocurrencies, then go [here](https://www.binance.com/en). 

If you want to automate interactions with Peatio Exchanges stick around.

# Source code

Link to **[Source Code](https://github.com/athenasaurav/Python_Peatio)**

# Features
   * Implementation of all General, Market Data and Account endpoints.
   * Simple handling of authentication
   * No need to generate timestamps yourself, the wrapper does it for you
   * Response exception handling
   * Symbol Depth Cache
   * Kline/Candle fetching function
   * Withdraw functionality
   * Deposit addresses
   * API Trading


## Quick Start

Register an account with a Peatio Exchange.

Generate an API Key and API Secret.

# Install
```
pip install Python_Peatio
```

# To Use

```
from Python_Peatio.Auth import Auth
auth = Auth(api_key, api_secret)
```

# Get Nonce and Signature
```
auth.signed_param()
```

# To place an BUY order
```
from Python_Peatio.Market import Market
Market = Market(api_key, api_secret)
order = Market.create_limit_order(
    URL='your http peatio url',
    market = 'symbol of cryptocurrency pair',
    side='buy',
    volume='0.002',
    price='38000')
```

# To place an SELL order
```
from Python_Peatio.Market import Market
Market = Market(api_key, api_secret)
order = Market.create_limit_order(
    URL='your http peatio url',
    market = 'symbol of cryptocurrency pair',
    side='Sell',
    volume='0.002',
    price='38000')
```

# To cancel an Buy or Sell order

```
from Python_Peatio.Market import Market
Market = Market(api_key, api_secret)
order = Market.id_cancel(
    URL='your http peatio url',
    id = buy or sell id to cancel)

```

## All the use cases will be uploaded soon
