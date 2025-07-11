import numpy as np

arr_1_D = np.array([1,2,3,4,5,6.0])
arr_2_D = np.array([[1,2,3],[4,5,6]])

print(arr_1_D.shape,arr_2_D.shape)
#shape代表数组的维度和数量

print(arr_1_D.size,arr_2_D.size)
#size代表数量

print(arr_1_D.dtype)
arr_1_D[-1] = 6.699
print(arr_1_D)
print(arr_1_D.dtype)