import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("합계:", arr.sum())  # 150
print("최솟값:", arr.min())  # 10
print("최댓값:", arr.max())  # 50
print("평균:", arr.mean())  # 30.0
print("표준편차:", arr.std())  # 14.142135623730951
print("분산:", arr.var())  # 200.0

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("전체 합계:", arr_2d.sum())  # 45

print("열 방향 합계:", arr_2d.sum(axis=0))  # [12 15 18]
print("행 방향 합계:", arr_2d.sum(axis=1))  # [ 6 15 24]

print("열 방향 최댓값:", arr_2d.max(axis=0))  # [7 8 9]
print("행 방향 최댓값:", arr_2d.max(axis=1))  # [3 6 9]