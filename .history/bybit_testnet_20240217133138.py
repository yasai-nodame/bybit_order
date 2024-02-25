from pybit.unified_trading import HTTP
import time

url = 'api-testnet.bybit.com'
api = 'Z9VeZzgUjHurFcd56a'


# # 現在時刻(ms)を取得
# def get_time():
#     session = HTTP(testnet=True)
#     get_time = session.get_server_time()['time']
#     return get_time


# #現在時刻取得
# current_time = int(time.time())

# interval_minutes = 15 * 60

# #encパラメーター計算
# end_time = current_time + interval_minutes


# ローソク足を取得
def get_kline():
        #現在時刻取得
    current_time = int(time.time())

    interval_minutes = 15 * 60

    #encパラメーター計算
    end_time = current_time + interval_minutes
    session = HTTP(testnet=True)
    
    params = (
        session.get_kline(
            category="linear",
            symbol="BTCUSDT",
            interval=15,
            start=current_time,
            end=end_time
        )
    )

    print(params)

get_kline()