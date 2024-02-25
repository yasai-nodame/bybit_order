from Crypto.PublicKey import RSA 

api_key = 'C:\\Users\\user\\bybit_automatic_trade\\api_text.pem'
api_secret = 'C:\\Users\\user\\bybit_automatic_trade\\test.pem'

with open(api_secret, 'r') as f:
    private_key = RSA.import_key(f.read())
    
    
    print(private_key)