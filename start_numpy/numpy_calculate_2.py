import numpy as np

array = np.arange(2, 14).reshape((3, 4))

print(array)
"""
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
"""

# ==========最值索引
print(np.argmin(array))  # 最小值索引 0
print(np.argmax(array))  # 最大值索引 11

# ==========平均值
print(np.mean(array))  # 7.5
print(array.mean())  # 7.5
print(np.average(array))  # 7.5

# ==========中位数
print(np.median(array))  # 7.5

# ==========累加
print(np.cumsum(array))
# [ 2  5  9 14 20 27 35 44 54 65 77 90]

# ==========累差
print(np.diff(array))
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""

# ==========定位非零元素位置
print(np.nonzero(array))
# (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]),
#  array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))

# ==========逐行排序
temp_a = np.arange(14, 2, -1).reshape((3, 4))
print(temp_a)
"""
[[14 13 12 11]
 [10  9  8  7]
 [ 6  5  4  3]]
"""
print(np.sort(temp_a))
"""
[[11 12 13 14]
 [ 7  8  9 10]
 [ 3  4  5  6]]
"""

# =========矩阵反向
print(np.transpose(temp_a))
print(temp_a.T)  # 另一种形式
"""
[[14 10  6]
 [13  9  5]
 [12  8  4]
 [11  7  3]]
"""

# =========矩阵截取
print(np.clip(temp_a, 5, 9))  # 所有小于5的元素等于5，所有大于9的元素等于9
"""
[[9 9 9 9]
 [9 9 8 7]
 [6 5 5 5]]
"""
