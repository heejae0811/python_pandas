import pandas as pd

data = [
    ['3R', 1510, 7.36],
    ['3SOFT', 1790, 1.65],
    ['ACTS', 1185, 1.28]
]
index = ['037730', '036360', '005760']
columns = ['종목명', '현재가', '등락률']

df = pd.DataFrame(data = data, index = index, columns = columns)

print(df)
print(df.iloc[0, 2])
print(df.loc['037730', '등락률'])

print(df.iloc[[0, 1], [0, 1]]) # [행번호], [열번호]
print(df.iloc[0:2, 0:2]) # 슬라이싱
print(df.loc[['037730', '036360'], ['종목명', '현재가']])
print(df.loc['037730':'036360', '종목명':'현재가']) # 슬라이싱