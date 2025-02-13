import numpy as np

data = [1, 2, 3, 4] # type = list
np_data = np.array(data) # type = numpy.ndarray

print(data)
print(np_data)

list_arr = data * 10
np_arr = np.array(data) * 10

print(list_arr)
print(np_arr)

multi_arr = np.array([
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400]
])

# 행 > 열 순서로 접근
print(multi_arr[0]) # [1 2 3 4]
print(multi_arr[1][2]) # 30
print(multi_arr[1, 2]) # 30
print(multi_arr[:, 3]) # [4 40 400]