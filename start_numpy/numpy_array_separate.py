# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 12:08
# @Author  : Bryce Liu
# @FileName: numpy_array_separate.py

import numpy as np

a_array = np.arange(12).reshape((3, 4))
print(a_array)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

# ========基本分割
# 纵向分割（按列分割）
print(np.split(a_array, 2, axis=1))
print(np.hsplit(a_array, 2))
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]),
 array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
"""


# 横向分割（按行分割）
print(np.split(a_array, 3, axis=0))
print(np.vsplit(a_array,3))
"""
[array([[0, 1, 2, 3]]),
 array([[4, 5, 6, 7]]),
 array([[ 8,  9, 10, 11]])]
"""

# =========不均等分割
print(np.array_split(a_array, 3, axis=1))
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]),
 array([[ 2],
       [ 6],
       [10]]),
 array([[ 3],
       [ 7],
       [11]])]
"""

