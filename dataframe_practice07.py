import pandas as pd
import pyupbit

pd.set_option('display.max_columns', None)  # 모든 열 출력
pd.set_option('display.width', None)  # 출력 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 너비 제한 해제

df = pyupbit.get_ohlcv('KRW-XRP')
df.drop(['volume', 'value'], axis = 1, inplace = True)
df['close_shift'] = df['close'].shift(1)
df['diff'] = df['close'] - df['close_shift']

print(df)