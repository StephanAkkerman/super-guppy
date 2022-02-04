from guppy import guppy
from ticker_data import crypto, stocks

ticker = 'AAPL'
crypto = False

if __name__ == "__main__":
    
    if crypto:
        df = crypto("Binance", ticker, "4h", since=None, limit=None)
    else:
        df = stocks(ticker, '1d')
        
    #guppy(df)