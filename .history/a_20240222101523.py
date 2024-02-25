from pybit.unified_trading import HTTP
import ccxt
from pprint import pprint 

api_key = 'XW604zcK1Z8aYj4sPV'
secret_key = 'ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'

session = HTTP(
    testnet=True,
    api_key=api_key,
    api_secret=secret_key
)

print(session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Market",
    qty="0.1",
))