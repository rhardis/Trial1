# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 22:00:44 2018

@author: Richard Hardis
"""

#import the alpha vantage timeseries package
from alpha_vantage.timeseries import TimeSeries

#Define the directory you are using on your computer.  Files will be saved here
directory = 'C:/Users/Richard Hardis/.spyder-py3/'

#Define the ticker you are interested in and the type of pull.
#Pull types can be 'intraday', 'daily', 'weekly', or 'monthly'
symbol = 'SPY'
pullType = 'intraday'
inter = '5min'

#Open a new timeseries object with the alpha vantage key code
ts = TimeSeries(key='1RJDU8R6RESLVE09', output_format='pandas')


#use the get_ function of the timeseries object with the appropriate period
if pullType == 'intraday':
    data1, meta_data1 = ts.get_intraday(symbol=symbol,interval=inter,outputsize='full')
elif pullType == 'daily':
    data1, meta_data1 = ts.get_daily_adjusted(symbol=symbol,outputsize='full')
elif pullType == 'weekly':
    data1, meta_data1 = ts.get_weekly_adjusted(symbol=symbol,outputsize='full')
elif pullType == 'monthly':
    data1, meta_data1 = ts.get_monthly_adjusted(symbol=symbol,outputsize='full')
else:
    print('Please enter a valid pull type')

data1.columns = ['Open','High','Low','Close','Volume']

#Save the dataframe in csv format   
data1.to_csv(directory+symbol+'.csv')

#Notify the user when complete
print('Saved csv')