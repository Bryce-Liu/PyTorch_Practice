# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 18:44
# @Author  : Bryce Liu
# @FileName: save_model.py

import torch

torch.manual_seed(1)

# =====create data
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())


def save_network():
    # build neural network
    torch.nn.Sequential(
        torch.nn.Linear(1,10),
        torch.nn.ReLU(),
        torch.nn.Linear(10,1)
    )
