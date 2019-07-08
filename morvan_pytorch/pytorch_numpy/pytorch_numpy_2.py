import torch
import numpy as np

# abs
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)

print(
        "=========abs==========="
        "\ntorch data:\n", torch.abs(tensor),
        "\nnumpy data:\n", np.abs(data)
)
"""
torch data:
 tensor([1., 2., 1., 2.])
numpy data:
 [1 2 1 2]
"""

# sin
print(
        "=========sin==========="
        "\ntorch data:\n", torch.sin(tensor),
        "\nnumpy data:\n", np.sin(data)
)
"""
torch data:
 tensor([-0.8415, -0.9093,  0.8415,  0.9093])
numpy data:
 [-0.84147098 -0.90929743  0.84147098  0.90929743]
"""

# matrix multiply

matrix_data = [[1, 2], [3, 4]]
matrix_tensor = torch.FloatTensor(matrix_data)

print(
        "=========matrix multiply==========="
        "\ntorch data:\n", torch.mm(matrix_tensor, matrix_tensor),
        "\nnumpy data:\n", np.matmul(matrix_data, matrix_data)
)
"""
torch data:
 tensor([[ 7., 10.],
        [15., 22.]])
numpy data:
 [[ 7 10]
 [15 22]]
"""