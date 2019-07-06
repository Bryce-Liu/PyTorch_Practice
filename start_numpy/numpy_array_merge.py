# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:40
# @Author  : Bryce Liu
# @FileName: numpy_array_merge.py

import numpy as np

a_array = np.array([1, 1, 1])
b_array = np.array([2, 2, 2])

# ==========垂直合并
c_array = np.vstack((a_array, b_array))
print(c_array)
"""
[[1 1 1]
 [2 2 2]]
"""
print(a_array.shape, b_array.shape, c_array.shape)
# (3,) (3,) (2, 3)

# ==========水平合并
d_array = np.hstack((a_array, b_array))
print(d_array)
# [1 1 1 2 2 2]
print(a_array.shape, b_array.shape, d_array.shape)
# (3,) (3,) (6,)

# ==========序列变为矩阵
e_array = a_array[np.newaxis, :]  # 横向矩阵
print(e_array)  # [[1 1 1]]
print(e_array.shape)  # (1, 3)

f_array = a_array[:, np.newaxis]  # 纵向矩阵
print(f_array)
"""
[[1]
 [1]
 [1]]
"""
print(f_array.shape)  # (3, 1)

# ==========将两个矩阵转制后再合并
ar_array = a_array[:, np.newaxis]
br_array = b_array[:, np.newaxis]
g_array = np.hstack((ar_array, br_array))
print(g_array)
"""
[[1 2]
 [1 2]
 [1 2]]
"""

# ==========指定合并方向
# 每个元素作为一行合并
print(np.concatenate((ar_array, br_array, br_array, ar_array), axis=0))
"""
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]
 [2]
 [2]
 [2]
 [1]
 [1]
 [1]]
"""
# 每个元素作为一列合并
print(np.concatenate((ar_array, br_array, br_array, ar_array), axis=1))
"""
[[1 2 2 1]
 [1 2 2 1]
 [1 2 2 1]]
"""
