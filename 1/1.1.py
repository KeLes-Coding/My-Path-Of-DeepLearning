from __future__ import print_function
import torch

# # 创建一个没有初始化的5*3矩阵
# x = torch.empty(5, 3)
# print(x)

# # 创建一个随机初始化矩阵
# y = torch.rand(5, 3)
# print(y)

# # 构造一个填满0且数据类型为long的矩阵
# z = torch.zeros(5, 3, dtype=torch.long)
# print(z)

# # 直接从数据构造张量：
# xx = torch.tensor([5.5, 3.5])
# print(xx)

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data)
