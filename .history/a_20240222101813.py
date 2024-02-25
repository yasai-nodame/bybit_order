from pybit import usdt_perpetual

API_KEY    = 'XW604zcK1Z8aYj4sPV'
API_SECRET = 'ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'

session = usdt_perpetual.HTTP(
    endpoint='https://api-testnet.bybit.com',
    api_key=API_KEY,
    api_secret=API_SECRET,
)

# 成行注文
session.place_active_order(
    symbol       = "BTCUSDT",
    order_type   = "Market",
    side         = "Buy",  # or "Sell" 
    qty          = 0.1,    # 購入量(BTC)
    # price      = 38000,   #成行なので注文価格は不要
    take_profit  = 49000.50,  #利食い価格
    stop_loss    = 37000.00,  #損切り価格
    reduce_only  = False,     # 利食/損切を設定する場合はFalse
    close_on_trigger = False, # 
    time_in_force    = "GoodTillCancel", #取引が成立するまで無期限で保有
    # order_link_id="cus_order_id_1",    # カスタムID: 任意で一意な36文字以内の文字列
    )