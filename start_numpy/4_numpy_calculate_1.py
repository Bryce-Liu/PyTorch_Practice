import numpy as np

# ==========数组计算
a_array = np.array([10, 20, 30, 40])
b_array = np.arange(4)
# print(a_array, b_array)  # [10 20 30 40] [0 1 2 3]

# 相加
result = a_array + b_array
# print(result)  # [10 21 32 43]

# 幂运算
result = b_array ** 2
# print(result)  # [0 1 4 9]

# 三角函数
result = 10 * np.sin(a_array)
# print(result)  # [-5.44021111  9.12945251 -9.88031624  7.4511316 ]

# 元素值比较
# print(b_array < 2)  # [ True  True False False]

# ==========矩阵计算
a_dim2 = np.array([[1, 1],
                   [0, 1]])
b_dim2 = np.arange(4).reshape((2, 2))
# print(a_dim2)
# print(b_dim2)
"""
[[1 1]
 [0 1]]
[[0 1]
 [2 3]]
"""
# 按元素位置逐个相乘
result = a_dim2 * b_dim2
# print(result)
"""
[[0 1]
 [0 3]]
"""

# 矩阵相乘
result = np.dot(a_dim2, b_dim2)
# print(result)
"""
[[2 4]
 [2 3]]
"""
# or
result = a_dim2.dot(b_dim2)
# print(result)  # 与上面结果一致

# =========矢量和标量运算
c_array = np.array([[1, 2], [3, 4]])
# print(1. / c_array)
"""
[[1.         0.5       ]
 [0.33333333 0.25      ]]
"""
# print(2. * c_array)
"""
[[2. 4.]
 [6. 8.]]
"""

# =========随机矩阵
random_a = np.random.random((2, 4))  # 元素值为0-1的随机array
# print(random_a)
"""
[[0.72452698 0.13651464 0.44600111 0.41655378]
 [0.89009035 0.7912297  0.78067892 0.95713937]]
"""

random_b = np.random.rand(2, 4)
# print(random_b)
"""
[[0.21914195 0.51772941 0.66419856 0.96328403]
 [0.45329901 0.29727969 0.80851175 0.50195666]]
"""

# =========聚合方法
# print(np.sum(random_a))
# 3.1339300057726764
# print(np.sum(random_a, axis=1))  # axis=1 每行聚合
# [2.1656187 0.9683113]
# print(np.sum(random_a, axis=0))  # axis=0 每列聚合
# [0.86301568 0.62897626 0.92527623 0.71666183]
# print(np.min(random_a))
# 0.11829881364496164
# print(np.max(random_a))
# 0.8069774128223589
