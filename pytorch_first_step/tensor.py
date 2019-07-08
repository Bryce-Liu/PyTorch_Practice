# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 10:37
# @Author  : Bryce Liu
# @FileName: tensor.py

from __future__ import print_function
import torch as t
import numpy as np

# =====构建5*3张量的tensor，仅分配空间而不执行初始化
x = t.Tensor(5, 3)
# print(x)
"""
tensor([[0.0000e+00, 2.0000e+00, 0.0000e+00],
        [2.0000e+00, 7.3787e+22, 2.4176e-12],
        [1.1625e+33, 8.9605e-01, 1.1632e+33],
        [5.6003e-02, 7.0374e+22, 2.7036e+23],
        [0.0000e+00, 2.0000e+00, 2.9018e-01]])
"""

# =====使用[0,1]均匀分布随机初始化二维数组
x = t.rand(5, 3)
# print(x)
"""
tensor([[0.4548, 0.8575, 0.8910],
        [0.6667, 0.7163, 0.2312],
        [0.6066, 0.9715, 0.1277],
        [0.2729, 0.0413, 0.7286],
        [0.0893, 0.0960, 0.1704]])
"""

# =====.size()查看张量的形状
print(x.size())
# torch.Size([5, 3])

# torch.size返回tuple对象的子类，因此具有tuple的属性
print(x.size()[0])  # 查看列的个数 5
print(x.size(0))  # 查看列的个数 5

# =====torch加法
# method 1
y = t.rand(5, 3)
result = x + y

# method2
result = t.add(x, y)

# method3
result = t.Tensor(5, 3)
t.add(x, y, out=result)

# print(result)
"""
tensor([[1.5341, 0.6817, 1.3371],
        [0.6140, 1.0844, 1.0712],
        [0.5905, 0.8645, 1.6925],
        [1.7706, 0.6545, 0.2032],
        [1.3980, 0.2591, 1.6758]])
"""

# =====torch dot加法
# 不修改tensor自身
# print("y.add(x)\n", y.add(x))
# print("y\n", y)
"""
y.add(x)
 tensor([[1.6267, 1.7004, 0.9850],
        [1.5846, 1.1986, 1.0140],
        [0.9833, 1.2860, 0.3580],
        [1.6231, 0.7997, 0.0132],
        [1.0124, 0.7475, 0.5056]])
y
 tensor([[0.7183, 0.9386, 0.5139],
        [0.6552, 0.8586, 0.0832],
        [0.8051, 0.9268, 0.3191],
        [0.8146, 0.7692, 0.0028],
        [0.1036, 0.0268, 0.0803]])
"""
# 修改tensor自身
# print("y.add_(x)\n", y.add_(x))
# print("y\n", y)
"""
y.add_(x)
 tensor([[1.6267, 1.7004, 0.9850],
        [1.5846, 1.1986, 1.0140],
        [0.9833, 1.2860, 0.3580],
        [1.6231, 0.7997, 0.0132],
        [1.0124, 0.7475, 0.5056]])
y
 tensor([[1.6267, 1.7004, 0.9850],
        [1.5846, 1.1986, 1.0140],
        [0.9833, 1.2860, 0.3580],
        [1.6231, 0.7997, 0.0132],
        [1.0124, 0.7475, 0.5056]])
"""

# =====tensor to numpy
a = t.ones(5)
# print(a)  # tensor([1., 1., 1., 1., 1.])

b = a.numpy()
# print(b)  # [1. 1. 1. 1. 1.]

c = np.ones(5)
d = t.from_numpy(c)
print(c)  # [1. 1. 1. 1. 1.]
print(d)  # tensor([1., 1., 1., 1., 1.], dtype=torch.float64)

# Tensor 与 numpy共享内存，两者的转换几乎不消耗资源
d.add_(1)
print(c)  # [2. 2. 2. 2. 2.]
print(d)  # tensor([2., 2., 2., 2., 2.], dtype=torch.float64)

# =====GPU Tensor
if t.cuda.is_available():
    print("cuda is available")
    x = x.cuda()
    y = y.cuda()
    print(x + y)
