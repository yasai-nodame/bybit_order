from pybit.unified_trading import WebSocket 
from time import sleep 

ws = WebSocket(
    testnet=True,
    channel_type="Market",
)

def handle_message(message):
    print(message)

ws.trade_stream(
    symbol="BTCUSDT",
    callback=handle_message
)

