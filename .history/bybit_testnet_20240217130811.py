from pybit.unified_trading import HTTP

url = 'api-testnet.bybit.com'
api = 'Z9VeZzgUjHurFcd56a'

def get_time():
    session = HTTP(testnet=True)
    get_time = session['retExtInfo']
    print(get_time)
    

get_time()