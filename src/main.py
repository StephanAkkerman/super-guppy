from guppy import guppy
from ticker_data import crypto, stocks

ticker = "AAPL"
timeframe = "1d"

is_crypto = False
crypto_exchange = "Binance"

if __name__ == "__main__":

    if is_crypto:
        df = crypto(crypto_exchange, ticker, timeframe, since=None, limit=70)
    else:
        df = stocks(ticker, timeframe, since=None, limit=70)

    print(guppy(df))
