from pybit.unified_trading import HTTP 

session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

print(session.get_coins_balance(
    accountType="FUND",
    coin="USDC"
))