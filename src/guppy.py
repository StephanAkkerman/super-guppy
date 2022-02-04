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

    # Keep only the close prices
    df = df[["close"]]

    # Remove all unnecessary rows
    try:
        df = df.iloc[len(df) - 70 :, :]
    except Exception:
        return None

    # Save EMAs in here
    guppies = []

    # Add EMAs
    for i in range(16):
        # 11 fast EMAs
        if i < 11:
            guppies.append({"kind": "ema", "length": 3 + i * 2})

        # 16 slow EMAs
        guppies.append({"kind": "ema", "length": 25 + i * 3})

    # Create your own Custom Strategy
    super_guppy = ta.Strategy(
        name="Super Guppy", description="7 Fast EMAs, 16 slow EMAs", ta=guppies
    )

    # Run the strategy over close prices
    df.ta.strategy(super_guppy)

    # We are only interested in the last row
    last_row = df.iloc[-1]

    # This could probably be done better
    # If each fast_EMA from 1 to 11 is bigger than the next
    colfast = None
    if (
        last_row["EMA_3"] > last_row["EMA_5"]
        and last_row["EMA_5"] > last_row["EMA_7"]
        and last_row["EMA_7"] > last_row["EMA_9"]
        and last_row["EMA_9"] > last_row["EMA_11"]
        and last_row["EMA_11"] > last_row["EMA_13"]
        and last_row["EMA_13"] > last_row["EMA_15"]
        and last_row["EMA_15"] > last_row["EMA_17"]
        and last_row["EMA_17"] > last_row["EMA_19"]
        and last_row["EMA_19"] > last_row["EMA_21"]
        and last_row["EMA_21"] > last_row["EMA_23"]
    ):
        colfast = True

    # If each fast_EMA from 1 to 11 is smaller than the next
    if (
        last_row["EMA_3"] < last_row["EMA_5"]
        and last_row["EMA_5"] < last_row["EMA_7"]
        and last_row["EMA_7"] < last_row["EMA_9"]
        and last_row["EMA_9"] < last_row["EMA_11"]
        and last_row["EMA_11"] < last_row["EMA_13"]
        and last_row["EMA_13"] < last_row["EMA_15"]
        and last_row["EMA_15"] < last_row["EMA_17"]
        and last_row["EMA_17"] < last_row["EMA_19"]
        and last_row["EMA_19"] < last_row["EMA_21"]
        and last_row["EMA_21"] < last_row["EMA_23"]
    ):
        colfast = False

    # If each slow_EMA from 1 to 16 is bigger than the next
    colslow = None
    if (
        last_row["EMA_25"] > last_row["EMA_28"]
        and last_row["EMA_28"] > last_row["EMA_31"]
        and last_row["EMA_31"] > last_row["EMA_34"]
        and last_row["EMA_34"] > last_row["EMA_37"]
        and last_row["EMA_37"] > last_row["EMA_40"]
        and last_row["EMA_40"] > last_row["EMA_43"]
        and last_row["EMA_43"] > last_row["EMA_46"]
        and last_row["EMA_46"] > last_row["EMA_49"]
        and last_row["EMA_49"] > last_row["EMA_52"]
        and last_row["EMA_52"] > last_row["EMA_55"]
        and last_row["EMA_55"] > last_row["EMA_58"]
        and last_row["EMA_58"] > last_row["EMA_61"]
        and last_row["EMA_61"] > last_row["EMA_64"]
        and last_row["EMA_64"] > last_row["EMA_67"]
        and last_row["EMA_67"] > last_row["EMA_70"]
    ):
        colslow = True

    if (
        last_row["EMA_25"] < last_row["EMA_28"]
        and last_row["EMA_28"] < last_row["EMA_31"]
        and last_row["EMA_31"] < last_row["EMA_34"]
        and last_row["EMA_34"] < last_row["EMA_37"]
        and last_row["EMA_37"] < last_row["EMA_40"]
        and last_row["EMA_40"] < last_row["EMA_43"]
        and last_row["EMA_43"] < last_row["EMA_46"]
        and last_row["EMA_46"] < last_row["EMA_49"]
        and last_row["EMA_49"] < last_row["EMA_52"]
        and last_row["EMA_52"] < last_row["EMA_55"]
        and last_row["EMA_55"] < last_row["EMA_58"]
        and last_row["EMA_58"] < last_row["EMA_61"]
        and last_row["EMA_61"] < last_row["EMA_64"]
        and last_row["EMA_64"] < last_row["EMA_67"]
        and last_row["EMA_67"] < last_row["EMA_70"]
    ):
        colslow = False

    # Bearish, Neutral, Bullish
    sentiment = [0, 0, 0]

    # Bullish Fast EMA
    if colfast and last_row["EMA_25"] > last_row["EMA_70"]:
        sentiment[2] += 50
    elif not colfast and last_row["EMA_25"] < last_row["EMA_70"]:
        sentiment[0] += 50

    # Slow EMA final colors
    if colslow:
        sentiment[2] += 50
    elif not colslow:
        sentiment[0] += 50

    if sentiment[0] == sentiment[2]:
        sentiment[1] = sentiment[0]

    most_certain = max(sentiment)
    prediction = ("🐻 - Bearish", "🦆 - Neutral", "🐂 - Bullish")[
        sentiment.index(most_certain)
    ]

    return f"{prediction} ({most_certain}%)"
