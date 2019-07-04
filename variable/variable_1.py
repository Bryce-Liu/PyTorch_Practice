import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1, 2], [3, 4]])
variable = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor * tensor)
v_out = torch.mean(variable * variable)

print(
        "t_out: \n", t_out,
        "\n",
        "v_out: \n", v_out
)
"""
t_out:
tensor(7.5000)
v_out:
tensor(7.5000, grad_fn=<MeanBackward0>)
"""

# 反向传递
v_out.backward()
print("反向传递结果:\n", variable.grad)
"""
tensor([[0.5000, 1.0000],
        [1.5000, 2.0000]])
"""

print("variable:\n", variable)
print("variable to tensor:\n", variable.data)
print("variable to numpy:\n", variable.data.numpy())
"""
variable:
 tensor([[1., 2.],
        [3., 4.]], requires_grad=True)
variable to tensor:
 tensor([[1., 2.],
        [3., 4.]])
variable to numpy:
 [[1. 2.]
 [3. 4.]]
"""
