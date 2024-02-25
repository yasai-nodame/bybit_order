from pybit.unified_trading import HTTP
session = HTTP(
    testnet=True,
    api_key="XXXXX",
    api_secret="XXXXX",
)
print(session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="0.1",
    price="15600",
    timeInForce="PostOnly",
    orderLinkId="spot-test-postonly",
    isLeverage=0,
    orderFilter="Order",
))