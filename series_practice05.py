from pandas import *

data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

print(s)

# 값 수정
s.iloc[0] = 0
s.loc['구구콘'] = 0
s['하겐다즈'] = 0

print(s)

# 값 삭제
s = s.drop('메로나')
s = s.drop(['구구콘', '하겐다즈'])

print(s)

# 값 추가
s.at["new1"] = 100
s.loc["new2"] = 200
s = concat([s, Series([300], index=["new3"])])

print(s)
