import pandas as pd
import pandas_ta as ta
import numpy as np

if __name__ == '__main__':

    # Downloaded from https://www.cryptodatadownload.com/data/binance/
    df = pd.read_csv('./data/Binance_BTCUSDT_d.csv', skiprows=1)
    df.drop(df.columns.difference(['close']), 1, inplace=True)
    
    # Flip it
    df = df[::-1].reset_index(drop=True)
    df = df.iloc[len(df)-70: , :]

    guppies = []
    
    # Add EMAs
    for i in range(16):
        # 11 fast EMAs
        if i < 11:
            guppies.append({"kind": "ema", "length": 3+i*2})

        # 16 slow EMAs
        guppies.append({"kind": "ema", "length": 25+i*3})

    # Create your own Custom Strategy
    super_guppy = ta.Strategy(
        name="Super Guppy",
        description="7 Fast EMAs, 16 slow EMAs",
        ta=guppies
    )
    
    # Run the strategy over close prices
    df.ta.strategy(super_guppy)
    
    last_row = df.iloc[-1]
    
    # If each fast_EMA from 1 to 11 is bigger than the next
    colfast = None
    for i in range(10):
        if last_row[f'EMA_{3+i*2}'] > last_row[f'EMA_{3+i*2+2}']:
            if i == 9:
                colfast = True
        else:
            break
    
    # If each fast_EMA from 1 to 11 is smaller than the next
    if colfast is None:
        for i in range(10):
            if last_row[f'EMA_{3+i*2}'] < last_row[f'EMA_{3+i*2+2}']:
                if i == 9:
                    colfast = False
            else:
                break
    
    # If each slow_EMA from 1 to 16 is bigger than the next
    colslow = None
    for i in range(15):
        if last_row[f'EMA_{25+i*3}'] > last_row[f'EMA_{25+i*3+3}']:
            if i == 14:
                colslow = True
        else:
            break
    
    # If each slow_EMA from 1 to 16 is smaller than the next
    if colslow is None:
        for i in range(15):
            if last_row[f'EMA_{25+i*3}'] < last_row[f'EMA_{25+i*3+3}']:
                if i == 14:
                    colslow = False
            else:
                break
            
    # Bearish, Neutral, Bullish    
    sentiment = [0,0,0]

    # Bullish Fast EMA
    if colfast and last_row['EMA_25'] > last_row['EMA_70']:
        sentiment[2] += 50
    elif not colfast and last_row['EMA_25'] < last_row['EMA_70']:
        sentiment[0] += 50
    
    # Slow EMA final colors
    if colslow:
        sentiment[2] += 50
    elif not colslow:
        sentiment[0] += 50
        
    if sentiment[0] == sentiment[2]:
        sentiment[1] = sentiment[0] 

    most_certain = max(sentiment)
    prediction = ("🐻 - Bearish", "🦆 - Neutral", "🐂 - Bullish")[sentiment.index(most_certain)]
    print(f"{prediction} ({most_certain}%)")