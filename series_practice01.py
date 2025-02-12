import pandas as pd
from pandas import Series

data = [0, 1, 2, 3] # type = list

p = pd.Series(data) # type = pandas.core.series.Series

print(type(data), type(p))
print(p)

data = [100, 200, 300]
index = ["월", "화", "수"]
s = Series(data, index)
print(s)

print("1", s.index)
print("1", s.values)
print("1", s.array)

name = ["메로나", "누가바", "빠삐코"]
price = [500, 800, 200]
menu = Series(name, price) # Series(data, index)
print(type(menu), menu)
