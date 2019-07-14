# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 18:44
# @Author  : Bryce Liu
# @FileName: save_model.py

import torch
import matplotlib.pyplot as plt

# torch.manual_seed(1)

# =====create data
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())


def save_network():
    # build neural network
    net1 = torch.nn.Sequential(
            torch.nn.Linear(1, 10),
            torch.nn.ReLU(),
            torch.nn.Linear(10, 1)
    )

    optimizer = torch.optim.SGD(net1.parameters(), lr=0.5)
    loss_func = torch.nn.MSELoss()

    # train
    for t in range(100):
        prediction = net1(x)
        loss = loss_func(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # plot result
    plt.figure(1, figsize=(10, 3))
    plt.subplot(131)
    plt.title("Net1")
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), "r-", lw=5)

    # save
    torch.save(net1, "net.pkl")  # 保存整个网络
    torch.save(net1.state_dict(), "net_params.pkl")  # 只保存网络中的参数

def restore_net():
    net2 = torch.load("net.pkl")
    prediction = net2(x)

    # plot result
    plt.subplot(132)
    plt.title("Net2")
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), "r-", lw=5)


def restore_params():
    net3 = torch.nn.Sequential(
            torch.nn.Linear(1, 10),
            torch.nn.ReLU(),
            torch.nn.Linear(10, 1)
    )
    net3.load_state_dict(torch.load("net_params.pkl"))
    prediction = net3(x)

    # plot result
    plt.subplot(133)
    plt.title("Net3")
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), "r-", lw=5)

    plt.show()


if __name__ == '__main__':
    # 保存 net1 (1. 整个网络, 2. 只有参数)
    save_network()

    # 提取整个网络
    restore_net()

    # 提取网络参数, 复制到新网络
    restore_params()
