import numpy as np

arr = np.array([10, 20, 30, 40, 50])
cond1 = arr > 10
cond2 = arr < 40

print(arr > 20) # [False False  True  True  True]
print(cond1) # [False  True  True  True  True]
print(cond2) # [ True  True  True False False]

print(arr[cond1 & cond2]) # [20 30]
print(arr[cond1 & cond2] / 10) # [2. 3.]