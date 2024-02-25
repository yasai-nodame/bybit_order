from pybit.unified_trading import HTTP

url = 'api-testnet.bybit.com'
api = 'Z9VeZzgUjHurFcd56a'


# 現在時刻(ms)を取得
def get_time():
    session = HTTP(testnet=True)
    get_time = session.get_server_time()['time']
    return get_time
    

# ローソク足を取得
def get_kline(time):
    session = HTTP(testnet=True)
    
    params = (
        session.get_kline(
            category="inverse",
            symbol="BTCUSD",
            interval=15,
            start=
        )
    )
