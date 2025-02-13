import pandas as pd
import pyupbit

pd.set_option('display.max_columns', None)  # 모든 열 출력
pd.set_option('display.width', None)  # 출력 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 너비 제한 해제

df = pyupbit.get_ohlcv('KRW-XRP')
# df['open'] += 100000

diff = df['open'] > df['close']

cond = df['close'] > df['open']

print(df[cond])