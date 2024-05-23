# Super Guppy Indicator
<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Supported versions">
  <img src="https://img.shields.io/github/license/StephanAkkerman/super-guppy.svg?color=brightgreen" alt="License">
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

---

This is a simple Python script for calculating the Super Guppy technical indicator. The code was inspired by the TradingView indicator of [JustUncleL](https://www.tradingview.com/script/q0s1bpoo-Super-Guppy-R1-2-by-JustUncleL/).

## Setup
You only need one thing to use this function, which is a pandas DataFrame consisting of 70 rows filled with close data of your favorite stock / cryptocurrency.
It will return the DataFrame filled with the EMAs + Guppy signal, where 1 = Buy, 0 = Hold, -1 = Sell. You can find this information in the "guppy" column of the returned DataFrame. This can be used for making strategies using the super guppy indicator. You can also use the EMAs values and colFinal columns to make your own strategy based on the values in those columns.

## Dependencies
The required packages to run this code can be found in the `requirements.txt` file. To run this file, execute the following code block:
```
$ pip install -r requirements.txt 
```
Alternatively, you can install the required packages manually like this:
```
$ pip install <package>
```

## How to run
- Clone the repository.
- Get a dataframe consisting of at least 70 rows of close prices.
- Call the super_guppy function located in `main.py` using this dataframe as parameter.
- See results.
