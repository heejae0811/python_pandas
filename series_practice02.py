import pandas as pd

data = [100, 200, 300]
index = ["월", "화", "수"]
s = pd.Series(data, index)

print(s.iloc[0]) # 100
print(s.iloc[1]) # 200
print(s.iloc[2]) # 300
print(s.iloc[3]) # IndexError

print(s.iloc[-1]) # 300
print(s.iloc[-2]) # 200
print(s.iloc[-3]) # 200
print(s.iloc[-4]) # IndexError

print(s.loc["월"]) # 100
print(s.loc["화"]) # 200
print(s.loc["수"]) # 300

# 인덱싱 (개별 값)
print(s.iloc[[0, 2]]) # 월 100 수 300
print(s.loc[["월", "수"]]) # 월 100 수 300

# 슬라이싱 (범위)
print(s.iloc[0:2]) # 월 100 화 200
print(s.loc["월":"화"]) # 월 100 화 200