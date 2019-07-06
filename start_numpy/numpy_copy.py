# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 12:18
# @Author  : Bryce Liu
# @FileName: numpy_copy.py

import numpy as np

a_array = np.arange(4)
print(a_array)  # [0 1 2 3]
b = c = d = a_array
print(b is a_array)  # True

# numpy array相当与可变对象
a_array[0] = 5
print(a_array)  # [5 1 2 3]
print(b)  # [5 1 2 3]

d[1:3] = [22, 33]
print(d)  # [ 5 22 33  3]
print(a_array)  # [ 5 22 33  3]

# 使用numpy.copy方法进行拷贝
b = a_array.copy()
a_array[3] = 666
print(a_array) # [  5  22  33 666]
print(b) # [ 5 22 33  3]
