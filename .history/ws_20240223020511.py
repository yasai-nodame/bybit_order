import json 
import threading 
from order import place_order 
from pybit.unified_trading import WebSocket
from time import sleep 
from datetime import datetime

def convert_timestamp_to_readable(timestamp_ms):
    timestamp_s = timestamp_ms / 1000
    date_time = datetime.utcfromtimestamp(timestamp_s)
    return date_time.strftime('%Y-%m-%d %H:%M:%S UTC')

ws = WebSocket(
    testnet=False,
    channel_type='spot'
)

def handle_message(message):
    if isinstance(message, str):
        message = json.loads(message)
    if 'data' in message and 'lastPrice' in message['data']:
        last_price = message['data']['lastPrice']
        print(f'Last Price: {last_price}')
        place_order(last_price)
    if 'data' in message:
        time = message['ts']
        print(f'Current time: {convert_timestamp_to_readable(time)}')
        print('-----------')
    sleep(3600)

ws.ticker_stream(
    symbol='BTCUSDT',
    callback=handle_message
)

while True:
    sleep(10)