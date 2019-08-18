# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:22
# @Author  : Bryce Liu
# @FileName: 6_numpy_index.py

import numpy as np

# ==========一维矩阵的索引
array = np.arange(3, 15)
# print(array)  # [ 3  4  5  6  7  8  9 10 11 12 13 14]
# print(array[3])  # 6

# ==========二维矩阵的索引
dim2_array = np.arange(3, 15).reshape((3, 4))
# print(dim2_array)
"""
[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
"""
# print(dim2_array[1][1])  # 8
# print(dim2_array[1, 1])  # 8
# print(dim2_array[2, :])  # 第3行所有元素
# [11 12 13 14]
# print(dim2_array[:, 2])  # 第3列所有元素
# [ 5  9 13]
# print(dim2_array[1, 1:3])  # 第二行index[1,3)的元素
# [8 9]


# =========条件索引
data = np.random.rand(3, 3)
print(data)
# [[0.2609872  0.72199878 0.1148983 ]
#  [0.05681223 0.46416415 0.24294159]
#  [0.27306214 0.53398118 0.67359752]]

condition_array = np.array([[4, 8, 1],
                            [2, 9, 6],
                            [7, 5, 3]])

grater_then_five = condition_array >= 5
print(grater_then_five)
# [[False  True False]
#  [False  True  True]
#  [ True  True False]]
print(data[grater_then_five])
# [0.72199878 0.46416415 0.24294159 0.27306214 0.53398118]

print(data[(condition_array >= 5) & (condition_array % 2 == 0)])
# [0.72199878 0.24294159]

# =========在矩阵中使用for循环
# 循环输出所有行
for row in dim2_array:
    print(row)
"""
[3 4 5 6]
[ 7  8  9 10]
[11 12 13 14]
"""

# 循环输出所有列
for column in dim2_array.T:
    print(column)
"""
[ 3  7 11]
[ 4  8 12]
[ 5  9 13]
[ 6 10 14]
"""

# 循环输出所有元素
print(dim2_array.flatten())  # flat相当于将二维转换为一维的数组
# [ 3  4  5  6  7  8  9 10 11 12 13 14]
for item in dim2_array.flat:
    print(item)
"""
3
4
5
6
7
8
9
10
11
12
13
14
"""
