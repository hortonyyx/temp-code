import numpy as np
print(np.__version__)


#numpy的维度概念:数组中的维是数组深度（嵌套数组）的一个级别————（有几个[]代表有几个维度，arr2有两个维度，只不过只有一组数）
arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([[1,2,3,4,5]])

print(arr_1.ndim)
print(arr_2.ndim)

#零维数组
arr_0_D = np.array(33)
#一维数组
arr_1_D = np.array([1,2,3,4])
#二维数组
arr_2_D = np.array([[1,2,3],[4,5,6]])

print(arr_0_D,arr_1_D,arr_2_D)

#创建维度数组
arr_5_D = np.array([5,5,5,5],ndmin=5)
print(arr_5_D,arr_5_D.ndim)