# 브로드캐스트

from pandas import *

low = Series([10, 200, 200, 400, 600])
high = Series([100, 300, 400, 500, 600])
diff = (high - low)

print(diff)
print(diff.loc[diff >= 100])

price = Series([93000, 82400, 99100, 81000, 72300], ['05/14', '05/15', '05/16', '05/17', '05/18'])

print(price)
print(price.loc[(price < 90000) & (price >= 80000)])