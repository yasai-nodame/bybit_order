from pybit.unified_trading import HTTP

url = 'api-testnet.bybit.com'
api = 'Z9VeZzgUjHurFcd56a'

def get_time():
    urls = url + '/v5/market/time'
    session = HTTP(url=urls,testnet=True)
    print(session.get_server_time())
    

get_time()