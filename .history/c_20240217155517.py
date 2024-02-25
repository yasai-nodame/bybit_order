import requests

url = "https://api-testnet.bybit.com/v5/asset/transfer/query-account-coins-balance?accountType=UNIFIED"

payload={}
headers = {
    'apiKey': 'V2IcREN12OgIyc3ELR',
    'secret': 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)