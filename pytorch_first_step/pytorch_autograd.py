# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 11:06
# @Author  : Bryce Liu
# @FileName: pytorch_autograd.py

"""
深度学习算法的本质是反向传播求导数
pytorch的Autograde实现反向传播求导的功能
"""
import torch as t
from torch.autograd import Variable

# =====新建Variable
x = Variable(t.ones(2, 2), requires_grad=True)
# print(x)
"""
tensor([[1., 1.],
        [1., 1.]], requires_grad=True)
"""

# 求和
y = x.sum()
# print(y)
# tensor(4., grad_fn=<SumBackward0>)

print(y.grad_fn)
# <SumBackward0 object at 0x1019b0668>

# =====反向传播，计算梯度
y.backward()
# print(x.grad)  # 计算得到每个值的梯度都是1
"""
tensor([[1., 1.],
        [1., 1.]])
"""

# =====反向传播的梯度累加, 反向传播前需要把梯度清零
y.backward()
# print(x.grad)
"""
tensor([[2., 2.],
        [2., 2.]])
"""
# 梯度清零
x.grad.data.zero_()
# print(x.grad)
"""
tensor([[0., 0.],
        [0., 0.]])
"""
y.backward()
# print(x.grad)
"""
tensor([[1., 1.],
        [1., 1.]])
"""

# =====Variable to Tensor
x = Variable(t.ones(4, 5))
y = t.cos(x)
x_tensor_cos = t.cos(x.data)
print(y)
"""
tensor([[0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
        [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
        [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
        [0.5403, 0.5403, 0.5403, 0.5403, 0.5403]])
"""
print(x_tensor_cos)
"""
tensor([[0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
        [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
        [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
        [0.5403, 0.5403, 0.5403, 0.5403, 0.5403]])
"""
