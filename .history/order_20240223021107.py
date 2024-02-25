import ccxt 
import config 

bybit = ccxt.bybit({
    'apiKey': config.API_KEY,
    'secret': config.API_SECRET
})

def place_order(price_str):
    try:
        price = float(price_str)
        if price > 1:
            print('Selling')
            order = bybit.create_order('BTCUSDT', 'market', 'buy', 10, 1.0001)
            print(order)
        elif price < 1:
            print('Buying')
            order = bybit.create_order('BITUSDT', 'market' , 'buy', 10, 0.9999)
            print(order)
    except ValueError:
        print(f'Invalid price format: {price_str}')
        pass 
    except Exception as e:
        print(f'An error occurred: {e}')
        pass 