from pybit.unified_trading import HTTP

session = HTTP(testnet=True)

info_mation = session.get_instruments_info(
    category="spot",
    symbol="BTCUSDT"
)