import pandas_ta as ta
import pandas as pd
import numpy as np


def guppy(df):
    """
    Uses a dataframe of at least 70 rows and a columned name 'close' as input
    Returns trend prediction based on Super Guppy
    """

    if type(df) != pd.DataFrame:
        if type(df) == list:
            df = pd.DataFrame(df, columns=["close"])
        elif type(df) == np.ndarray:
            df = pd.DataFrame(data=df, columns=["close"])
        else:
            print(f"Your input type is not supported: {type(df)}")

    # Make the fast and slow EMAs
    guppies = [{"kind": "ema", "length":f} for f in list(range(3, 25, 2))]
    guppies += [{"kind": "ema", "length":s} for s in list(range(25, 73, 3))]

    # Create your own Custom Strategy
    super_guppy = ta.Strategy(
        name="Super Guppy", 
        description="7 Fast EMAs, 16 slow EMAs", 
        ta=guppies
    )

    # Run the strategy over close prices
    df.ta.strategy(super_guppy, close="close")
    
    # Remove all NaN rows, which are the first 70 rows
    df = df.dropna()
    
    # To ignore the warning
    df = df.copy()
    
    df['colfastL'] = np.where((df["EMA_3"] > df["EMA_5"]) &
                             (df["EMA_5"] > df["EMA_7"]) &
                             (df["EMA_7"] > df["EMA_9"]) &
                             (df["EMA_9"] > df["EMA_11"]) &
                             (df["EMA_11"] > df["EMA_13"]) &
                             (df["EMA_13"] > df["EMA_15"]) &
                             (df["EMA_15"] > df["EMA_17"]) &
                             (df["EMA_17"] > df["EMA_19"]) &
                             (df["EMA_19"] > df["EMA_21"]) &
                             (df["EMA_21"] > df["EMA_23"]), True, False)
        
    df['colfastS'] = np.where((df["EMA_3"] < df["EMA_5"]) &
                         (df["EMA_5"] < df["EMA_7"]) &
                         (df["EMA_7"] < df["EMA_9"]) &
                         (df["EMA_9"] < df["EMA_11"]) &
                         (df["EMA_11"] < df["EMA_13"]) &
                         (df["EMA_13"] < df["EMA_15"]) &
                         (df["EMA_15"] < df["EMA_17"]) &
                         (df["EMA_17"] < df["EMA_19"]) &
                         (df["EMA_19"] < df["EMA_21"]) &
                         (df["EMA_21"] < df["EMA_23"]), True, False)
        
    df["colslowL"] = np.where((df["EMA_25"] > df["EMA_28"]) &
                                  (df["EMA_28"] > df["EMA_31"]) &
                                  (df["EMA_31"] > df["EMA_34"]) &
                                  (df["EMA_34"] > df["EMA_37"]) &
                                  (df["EMA_37"] > df["EMA_40"]) &
                                  (df["EMA_40"] > df["EMA_43"]) &
                                  (df["EMA_43"] > df["EMA_46"]) &
                                  (df["EMA_46"] > df["EMA_49"]) &
                                  (df["EMA_49"] > df["EMA_52"]) &
                                  (df["EMA_52"] > df["EMA_55"]) &
                                  (df["EMA_55"] > df["EMA_58"]) &
                                  (df["EMA_58"] > df["EMA_61"]) &
                                  (df["EMA_61"] > df["EMA_64"]) &
                                  (df["EMA_64"] > df["EMA_67"]) &
                                  (df["EMA_67"] > df["EMA_70"]), True, False)
        
    df["colslowS"] = np.where((df["EMA_25"] < df["EMA_28"]) &
                                  (df["EMA_28"] < df["EMA_31"]) &
                                  (df["EMA_31"] < df["EMA_34"]) &
                                  (df["EMA_34"] < df["EMA_37"]) &
                                  (df["EMA_37"] < df["EMA_40"]) &
                                  (df["EMA_40"] < df["EMA_43"]) &
                                  (df["EMA_43"] < df["EMA_46"]) &
                                  (df["EMA_46"] < df["EMA_49"]) &
                                  (df["EMA_49"] < df["EMA_52"]) &
                                  (df["EMA_52"] < df["EMA_55"]) &
                                  (df["EMA_55"] < df["EMA_58"]) &
                                  (df["EMA_58"] < df["EMA_61"]) &
                                  (df["EMA_61"] < df["EMA_64"]) &
                                  (df["EMA_64"] < df["EMA_67"]) &
                                  (df["EMA_67"] < df["EMA_70"]), True, False)
    
    # Fast EMA color rules
    df["colFinal"] = np.where((df["colfastL"] == True) & (df["EMA_25"] > df["EMA_70"]), "aqua", "gray") # Aqua = Buy
    df["colFinal"] = np.where((df["colslowL"] == True) & (df["EMA_25"] < df["EMA_70"]), "blue", df["colFinal"]) # Blue = Sell
    
    df["colFinal2"] = np.where((df["colfastL"] == True), "lime", "gray") # Lime = Buy
    df["colFinal2"] = np.where((df["colslowS"] == True), "red", "gray") # Red = Sell
    
    # Custom buy signals, 1 = Buy, 0 = Hold, -1 = Sell
    df["guppy"] = np.where((df["colFinal"] == "aqua") | (df["colFinal2"] == "lime"), 1, 0) # Aqua = Buy
    df["guppy"] = np.where((df["colFinal"] == "blue") | (df["colFinal2"] == "red"), -1, df["guppy"])
    df["guppy"] = np.where((df["colFinal"] == "gray") & (df["colFinal2"] == "gray"), 0, df["guppy"])
    
    return df