import requests

def get_btc():
    URL = 'https://api.binance.com/api/v1/trades?symbol=ETHBTC'
    r = requests.get(URL).json()
    price = r[-1]['price']
    qty = r[-1]['qty']
    return 'Было куплено '+ str(qty)+ ' эфира по цене '+ str(price) + 'BTC за 1 эфир.'










