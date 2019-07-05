import torch
import torch.nn.functional as f
from torch.autograd import Variable
import matplotlib.pyplot as plt


# make test data
t_data = torch.linspace(-5, 5, 200)
t_data = Variable(t_data)


# create activation function(relu, sigmoid, tanh, softplus)
np_data = t_data.data.numpy()
y_relu = f.relu(t_data).data.numpy()
y_sigmoid = f.sigmoid(t_data).data.numpy()
y_tanh = f.tanh(t_data).data.numpy()
y_softplus = f.softplus(t_data).data.numpy()


# show data
plt.figure(1, figsize=(8, 6))
# =========relu=========
plt.subplot(221)  #要生成两行两列，这是第一个图plt.subplot('行','列','编号')，这里看来","可省略
plt.plot(np_data, y_relu, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')
# =========sigmoid=========
plt.subplot(222)
plt.plot(np_data, y_sigmoid, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')
# =========tanh=========
plt.subplot(223)
plt.plot(np_data, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')
# =========softplus=========
plt.subplot(224)
plt.plot(np_data, y_softplus, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()
