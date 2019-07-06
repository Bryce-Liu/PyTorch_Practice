import numpy as np

int_array = np.array([1, 2, 3], dtype=np.int)  # 定义array与格式
print(int_array)  # [1 2 3]
print(int_array.dtype)  # int64

f_array = np.array([4, 5, 6], dtype=np.float64)  # 定义array与格式
print(f_array)  # [4. 5. 6.]
print(f_array.dtype)  # float64

dim2_array = np.array([[1, 2, 3],
                       [4, 5, 6]])
print(dim2_array)
"""
[[1 2 3]
 [4 5 6]]
"""

zero_array = np.zeros((3, 4))  # 全零矩阵
print(zero_array)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

one_array = np.ones((3, 4))  # 全1矩阵
print(one_array)
"""
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

empty_array = np.empty((3, 4))  # 全空矩阵
print(empty_array)
"""
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

range_array = np.arange(0, 12, 2)  # 生成一维矩阵
print(range_array)  # [ 0  2  4  6  8 10]
temp_array = range_array.reshape((2, 3))  # 变换矩阵维度
print(temp_array)
"""
[[ 0  2  4]
 [ 6  8 10]]
"""

line_array = np.linspace(1, 10, 4)  # 生成线段
print(line_array)  # [ 1.  4.  7. 10.]
temp_array = line_array.reshape((2, 2))
print(temp_array)
"""
[[ 1.  4.]
 [ 7. 10.]]
"""
