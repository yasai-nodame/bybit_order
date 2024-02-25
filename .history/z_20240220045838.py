from Crypto.PublicKey import RSA 

api_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu/RcLVfbvIDC8InsJPBDKmZTUhF2Ue6sV+1anxc4l7hKsj2AI4qfmK4Oj4cAMDLuMf0x/hK5EDtfzswvDudst/WPQZ4Q/btCCEN3rvuB0YkcnZuQt/da3k3vsj3VU0KsszlgGWSEUYue5vfzhddm+xRmPfEBB9KljK44DL5JRaSmZuqWDlkIxakajmmV7tIqx/GbnUWe2H+qpLVFcOi1iusWG37d0LgCI8Mw66HJjdktR05mAJCPDYs9AWqxH51GeAjqSB6ud+HiYB0l8gDTxedryDI17flwG7ZaAJMoem5mgI6TDyQppy2HtfgNJBwC+yhmuzg7NlwFfhO+4dwLIQIDAQAB'
api_secret = 'C:\\Users\\user\\bybit_automatic_trade\\test.txt'

with open(api_secret, 'r') as f:
    private_key = RSA.import_key(f.read())
    
    
    print(private_key)