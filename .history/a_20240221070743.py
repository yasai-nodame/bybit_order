from pybit.unified_trading import HTTP
import ccxt
from pprint import pprint 

api_key = 'V2IcREN12OgIyc3ELR'
secret_key = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'

print('CCXT Version:', ccxt.__version__)

exchange = ccxt.bybit({
    "enableRateLimit":True,
    "apiKey":api_key, 
    "secret":secret_key,
    "options":{
        "defaultType":"swap"
    }
})

markets = exchange.load_markets()

exchange.verbose = True 
balance = exchange.fetch_balance()
pprint(balance)
exchange.create_limit_buy_order(symbol='BTCUSDT', amount=0.1,)