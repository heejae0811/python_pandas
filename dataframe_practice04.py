import pandas as pd
import pyupbit

# 모든 열과 행을 출력하도록 설정
# pd.set_option('display.max_rows', None)  # 모든 행 출력
pd.set_option('display.max_columns', None)  # 모든 열 출력
pd.set_option('display.width', None)  # 출력 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 너비 제한 해제

df = pyupbit.get_ohlcv('KRW-BTC')
df['range'] = df['high'] - df['low']
df.drop('value', axis = 1) # 원본 적용 x
df.drop(['value', 'range', 'volume'], axis = 1, inplace = True) # 원본 적용

date = '2025-02-13'
dt = pd.to_datetime(date)
df.loc[dt] = [100, 200, 100, 150] # 로우 추가
df.loc[dt] = [1000, 2000, 1000, 1500] # 로우 추가
df.drop(df.index[-2], axis = 0, inplace = True) # 로우 삭제

print(df)