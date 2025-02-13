import pandas as pd

data = ['2025-01-01', '2024-01-01']
print(type(data)) # list

dt = pd.to_datetime(data)
print(type(dt)) # pandas.core.indexes.datetimes.DatetimeIndex