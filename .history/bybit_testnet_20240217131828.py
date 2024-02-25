from pybit.unified_trading import HTTP
import time

url = 'api-testnet.bybit.com'
api = 'Z9VeZzgUjHurFcd56a'


# # 現在時刻(ms)を取得
# def get_time():
#     session = HTTP(testnet=True)
#     get_time = session.get_server_time()['time']
#     return get_time

#現在時刻取得
current_time = int(time.time())

interval_minutes = 15

#encパラメーター計算
end_time = current_time + timedelta(minutes=interval_minutes)
print(current_time)
print(end_time)

# # ローソク足を取得
# def get_kline():
#     session = HTTP(testnet=True)
    
#     params = (
#         session.get_kline(
#             category="inverse",
#             symbol="BTCUSD",
#             interval=interval_minutes,
#             start=time,
#             end=
#         )
#     )
