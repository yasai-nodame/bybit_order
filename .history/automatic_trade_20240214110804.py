import requests 

# Bybit APIのエンドポイント
endpoint = 'https://api-testnet.bybit.com'

# Bybit APIキー
api_key = 'Z9VeZzgUjHurFcd56a'

# リクエストヘッダーにAPIキーを追加
headers = {
    'Content-Type': 'application/json'
}

# レスポンスの確認
if response.status_code == 200:
    #データの取得
    candle_data = response.json()
    print(candle_data)
else:
    print('エラー:',response.status_code)