import pandas as pd

data = [100, 200, 300]
index = ['월', '화', '수']
s = pd.Series(data = data, index = index)
print(s)

# 데이터 추가
s['목'] = 400
s.loc['금'] = 500
print(s)

# 데이터 삭제 drop: 원본을 삭제하지 않아서 재할당하거나 옵션 사용할 것
s = s.drop('목')
s.drop('금', inplace = True)
print(s)

s['월'] = 1000
s.loc['화'] = 2000
s.iloc[2] = 3000
print(s)


