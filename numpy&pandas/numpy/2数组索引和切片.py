import numpy as np

array_1_D = np.array([1,2,3,4,5])
print(array_1_D[3])

array_2_D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2_D[:,1],array_2_D[2,-1])

array_3_D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,0,0]],[[10,11,12],[13,14,15]]])
print(array_3_D[:,1,-2],array_3_D[1,-1,-2])

#索引可以理解为，有几个维度，就分别需要在几个维度上的索引

#切片

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])