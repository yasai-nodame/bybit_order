from pybit.unified_trading import HTTP
import ccxt
from pprint import pprint 

api_key = 'XW604zcK1Z8aYj4sPV'
secret_key = 'ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'

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