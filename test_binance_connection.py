import ccxt
import os
from pprint import pprint

print('CCXT Version:', ccxt.__version__)

LD_API_KEY = os.getenv("API_KEY_BINANCE")
LD_API_SECRET = os.getenv("API_SECRET_BINANCE")

conn_exchange = ccxt.binance({
       'apiKey': LD_API_KEY,
       'secret': LD_API_SECRET,
       'enableRateLimit': True,
       'options': { 'defaultType': 'future' },
   })

conn_exchange.load_markets()

conn_exchange.verbose = True
pprint(conn_exchange.fetch_balance())