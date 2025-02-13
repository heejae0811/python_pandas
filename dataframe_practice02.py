import pandas as pd

data = [
    [157000, 39.88, 4.38],
    [51300, 8.52, 1.45],
    [68800, 10.03, 0.87],
    [140000, 228.38, 2.16]
]
index =['네이버', '삼성전자', '엘지전자', '카카오']
columns = ['종가', 'PER', 'PBR']

df = pd.DataFrame(data = data, index = index, columns = columns)
# print(df)
#
# # 컬럼 선택
# print(df['종가'])
# print(df[['PER', 'PBR']])

# 행 선택
# print(df.iloc[0]) # 행번호
# print(df.loc['네이버']) # 인덱스 값

# print(df.iloc[[0, 3]])
# print(df.loc[['네이버', '카카오']])

print(df.iloc[0:2])
print(df.loc['네이버':'엘지전자'])