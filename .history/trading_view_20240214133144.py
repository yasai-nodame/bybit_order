from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta 
from tradingview_ta import TradingView

btc = TA_Handler(
    symbol='MAGICRABBITUSDT_5FDF82',
    screener='crypto',
    exchange='PANCAKESWAP',
    interval=Interval.INTERVAL_15_MINUTES
)

analysis = btc.get_analysis()

print(analysis)