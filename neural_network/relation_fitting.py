import torch
import matplotlib.pyplot as plt
import torch.nn.functional as f

# ========create data set
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())  # y = a * x^2 + b 其中torch.rand()提供噪音

plt.scatter(x.data.numpy(), y.data.numpy())


# ========create neural network
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
# print(net)
"""
Net(
  (hidden): Linear(in_features=1, out_features=10, bias=True)
  (predict): Linear(in_features=10, out_features=1, bias=True)
)
"""

# ========train neural network
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)  # 传入 net 的所有参数, 学习率
loss_func = torch.nn.MSELoss()  # 预测值和真实值的误差计算公式 (均方差)

plt.ion()

for t in range(100):
    prediction = net(x)  # 输入训练数据，输出预测值
    loss = loss_func(prediction, y)  # 计算均方差
    optimizer.zero_grad()  # 清空残余更新参数值
    loss.backward()  # 误差反向传递
    optimizer.step()  # 将参数更新值施加到 net 的 parameters 上

    # ========show training process
    if t % 5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), "r-", lw=5)
        plt.text(0.5, 0, "Loss=%.4f" % loss.data.numpy(), fontdict={"size": 20, "color": "red"})
        plt.pause(0.1)

plt.ioff()
plt.show()
