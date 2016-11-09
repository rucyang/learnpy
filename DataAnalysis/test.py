from pandas import DataFrame, Series
# import pandas as pd
import numpy as np
import pandas.io.data as web


# 汇总和计算描述统计

df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]], index=list('abcd'),
               columns=['one', 'two'])
print(df)
print(df.sum())
print(df.sum(axis=1))  # axis=1将按行计算，axis=0将按列计算
print(df.mean(axis=1, skipna=False))
print(df.describe())

obj = Series(['a', 'a', 'b', 'c'] * 4)

print(obj)
print(obj.describe())

all_data = {}


for ticker in ['AAP', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')


price = DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.items()})
volume = DataFrame({tic: data['Volume']
                    for tic, data in all_data.items()})

returns = price.pct_change()
print(price.tail())

data = DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
print(data)
