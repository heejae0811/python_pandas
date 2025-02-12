import pandas as pd

data = [100, 200, 300]
index = ["월", "화", "수"]
s = pd.Series(data, index)
print(s)

print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])

print(s.loc["월"])
print(s.loc["화"])
print(s.loc["수"])

print(s.iloc[0:2])
print(s.loc["월":"화"])

print(s.iloc[[0, 2]])
