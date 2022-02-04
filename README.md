# Super_Guppy
This is a simple script Python for calculating the Super Guppy technical indicator.\
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![MIT License](https://img.shields.io/github/license/StephanAkkerman/Super_Guppy.svg?color=brightgreen)](https://opensource.org/licenses/MIT)

---

## Setup
You only need one thing for using this function, that is a pandas dataframe consisting of 70 rows filled with close data of your favorite stock / cryptocurrency.
The function will output a certainty about the current trend, if this is not what you are looking for, you can easily change the function to still calculate the super guppy but return something else.

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
- Get a dataframe consisting of 70 rows of close prices.
- Call the super_guppy function located in `main.py` using this dataframe as parameter.
- See results.
