from pybit.unified_trading import HTTP
import time


#現在時刻取得
current_time = int(time.time())

interval_minutes = 15 * 60

#encパラメーター計算
end_time = current_time + interval_minutes


# ローソク足を取得
def get_kline():
    session = HTTP(testnet=True)
    
    print((
        session.get_kline(
            category="inverse",
            symbol="BTCUSD",
            interval=15,
            start=current_time,
            end=end_time
        )
    ))

get_kline()