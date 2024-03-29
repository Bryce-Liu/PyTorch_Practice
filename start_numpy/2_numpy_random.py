# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 10:55
# @Author  : Bryce Liu
# @FileName: 2_numpy_random.py

import numpy as np

# ============生成两行四列(0, 1)的随机矩阵
array = np.random.rand(2, 4)
# print(array)
# [[0.46758763 0.45855258 0.03808093 0.57810018]
#  [0.00400674 0.8940892  0.38428168 0.67672631]]

# ============生成两行四列(-2, 2)随机整数矩阵
array = np.random.randint(-2, 2, size=(2, 4))
# print(array)
# [[ 1  1  1 -1]
#  [-1 -2  0  1]]

# ============生成两行四列(-2, 2)随机浮点数矩阵
array = np.random.uniform(-2, 2, size=(2, 4))
# print(array)
# [[ 0.40867492 -1.79369331  1.40714446  1.2067595 ]
#  [ 0.08770933 -0.02104837 -1.20283084  1.45371199]]
