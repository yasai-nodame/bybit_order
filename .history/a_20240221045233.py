from pybit.unified_trading import HTTP
session = HTTP(
    testnet=True,
    api_key="V2IcREN12OgIyc3ELR",
    api_secret="KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT",
)
print(session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="1.0",
    price="10000",
    timeInForce="PostOnly",
    orderLinkId="spot-test-postonly",
    isLeverage=0,
    orderFilter="Order",
))