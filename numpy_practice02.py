import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
c = np.array([1, 2, 3, 4, 5]) # a와 c를 연산하면 ValueError가 발생

print(a + b) # [11 22 33]
print(a - b) # [9 18 27]
print(a * b) # [10 40 90]
print(a / b) # [10. 10. 10.]
print(a % b) # [0 0 0]
print(a + 5) # [15, 25, 35]

data1 = np.array([1, 2, 3]) # 1D 배열
data2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]) # 2D 배열

print(data1[0]) # 1
print(data2[0]) # [10 20 30]

print(data2[0, 2]) # 30
print(data2[0][2]) # 30

print(data1[1] * 10) # 20
print(data2[1] * 10) # [400 500 600]

print(data1 + data2) # [[11 22 33] [41 52 63] [71 82 93]]