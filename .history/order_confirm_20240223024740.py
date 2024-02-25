import requests 
import config 

api_key = config.API_KEY

def get_order(order_id)
    url = f'https://api-testnet.bybit.com/spot/v3/private/order?orderLinkId={order_id}'
    