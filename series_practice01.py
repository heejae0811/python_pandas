from pandas import Series
import pandas as pd

data = ['가', '나', '다', '라'] # type = list
s = pd.Series(data) # type = pandas.core.series.Series
print(s)

data = [100, 200, 300]
index = ["월", "화", "수"]
s = Series(data, index)
print(s)
print(s.index, s.values, s.array)

name = ["메로나", "누가바", "빠삐코"]
price = [500, 800, 200]
menu = Series(name, price)
print(menu)