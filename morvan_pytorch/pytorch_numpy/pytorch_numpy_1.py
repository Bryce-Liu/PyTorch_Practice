import torch
import numpy as np


np_data = np.arange(6).reshape((2,3))  # reshape成两行三列的数据
# numpy to torch
torch_data = torch.from_numpy(np_data)
# torch to numpy
torch2numpy = torch_data.numpy()

print(
    "numpy data:\n", np_data,
    "\n",
    "torch data:\n", torch_data,
    "\n",
    "numpy data:\n", torch2numpy
)
"""
numpy data:
 [[0 1 2]
 [3 4 5]]
torch data:
 tensor([[0, 1, 2],
        [3, 4, 5]])
numpy data:
 [[0 1 2]
 [3 4 5]]
"""