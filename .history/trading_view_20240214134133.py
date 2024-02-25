from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta 
from tradingview_ta import TradingView

handler  = TA_Handler(
    symbol='MAGICRABBITUSDT_5FDF82',
    screener='crypto',
    exchange='PANCAKESWAP',
    interval=Interval.INTERVAL_15_MINUTES
)

analysis = handler.get_analysis()
print(analysis.summary)

get_macd = analysis.indicators['MACD']
print(f'MACD: {get_macd}')