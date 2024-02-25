from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta 
from tradingview_ta import TradingView

btc = TA_Handler(
    symbol='MAGICRABBITUSDT_5FDF82',
    screener='crypto',
    exchange='PANCAKESWAP',
    
)

print(tradingview_ta.__version__)