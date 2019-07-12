# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 18:34
# @Author  : Bryce Liu
# @FileName: quick_neural_network.py

import torch
import torch.nn.functional as f


# old way
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)  # 输出层线性输出

    def forward(self, x):  # 重写torch.nn.Module的forward方法
        x = f.relu(self.hidden(x))  # 激励函数relu
        x = self.predict(x)  # 输出值
        return x


net = Net(n_feature=1, n_hidden=10, n_output=1)

# new way
net2 = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1)
)

print(net)
"""
Net(
  (hidden): Linear(in_features=1, out_features=10, bias=True)
  (predict): Linear(in_features=10, out_features=1, bias=True)
)
"""
print(net2)
"""
Sequential(
  (0): Linear(in_features=1, out_features=10, bias=True)
  (1): ReLU()
  (2): Linear(in_features=10, out_features=1, bias=True)
)
"""
