from torch import nn
import torch
import matplotlib.pyplot as plt
conv1 = nn.Conv2d(3,16,3)

# 使用标注正态分布初始化权重
torch.manual_seed(12)
nn.init.normal_(conv1.weight,mean=0,std=1) #随机生成0，1正态分布
plt.figure(figsize=(8,6))
plt.hist(conv1.weight.data.numpy().reshape((-1,1)),bins = 30)
plt.show()
