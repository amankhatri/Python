__author__ = 'Aman'
#how to get the min , max of dictionary and how to sort dictionary
#creating a set
stocks = {
     'Goog':520.54,
     'FB':76.45,
     'YHOO': 39.28,
     'AMZN': 306.21,
     'AAPL':99.76
 }

#we will use zip fuction we will consider the name of the company as list one and values of stocks at list 2
#you can not sort dictionary by default however you can sort the zip , so if you give zip name first the list will be
#sorted by name if you give them values it will be sorted by values
print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.keys(),stocks.values())))