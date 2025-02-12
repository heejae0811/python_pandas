import numpy as np

data = [1, 2, 3, 4] # type = numpy.ndarray
arr = np.array(data) * 10

# print(type(arr), arr)

data1 = np.array([
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400]
])

# 행 단위로 인덱싱
# 행 > 열 순서로 접근

print(data1[0]) # [1 2 3 4]
print(data1[0][1]) # 2
print(data1[0, 1]) # 2
print(data1[:, 0]) # [1 10 100]