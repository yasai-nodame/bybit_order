from pybit.unified_trading import HTTP

if __name__ == "__main__":
    session = HTTP(
        api_key='XW604zcK1Z8aYj4sPV',
        api_secret='ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'
    )
    
    r = session.get_tickers(category="spot",symbol="BTCUSDT")
    
    o = session.place_order(
        category="spot",
        symbol="BTCUSDT",
        side="Buy",
        orderType="Limit",
        qty="0.1",
        price="15600",
        TimeInForce="PostOnly",
        orderLinkId="spot-test-postonly",
        isLeverage=0,
        orderFilter="Order",
    )