#!/usr/bin/env python
# coding: utf-8
#Must install pandas-datareader

import pandas as pd
from pandas_datareader import data as wb

#Extract and check asset data with yahoo's API, in this case MSFT Stocks, starting 2000/1/1
MSFT_DATA = wb.DataReader('MSFT', 'yahoo', ('2000/1/1'))
MSFT_DATA.head()
MSFT_DATA.tail()

#Creating a table with values provided by ROR formula
import matplotlib.pyplot as plt

MSFT_DATA['Simple Rates Of Return'] = (MSFT_DATA['Adj Close']/MSFT_DATA['Adj Close'].shift(1)) - 1
MSFT_DATA['Simple Rates Of Return'].tail()

#Generating graphic
sror_msft = MSFT_DATA['Simple Rates Of Return'].plot(figsize=(8,5))

#Obtaining anual average rate of return
#.mean gets daily average
d_average_r = MSFT_DATA['Simple Rates Of Return'].mean()
d_average_r

a_average_r = MSFT_DATA['Simple Rates Of Return'].mean()*250 #250 trading days in a year
a_average_r

#Rounding and presentation in percentage
avg_r_a = str(round(a_average_r, 5)* 100) + '%'
Print = ("Microsoft's anual average rate of return, from 2000/1/1 is " + avg_r_a)

