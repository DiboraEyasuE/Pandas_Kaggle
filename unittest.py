import pandas_datareader.data as web
import unittest

def get_stock_data(ticker):
    df = web.DataReader(ticker, "yahoo")
    return df

unittest.main()