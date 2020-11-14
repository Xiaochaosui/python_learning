import torch
import torch.utils.data as Data
from torchvision.datasets import FashionMNIST

import  torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

# 以导入数据集FashionMNIST

train_data = FashionMNIST(
    root='./data/FashionMNIST',
    train= True,
    transform = transforms.ToTensor(),
    download = False
)

# 定义一个数据加载器
batchSize = 64
train_loader = Data.DataLoader(
    dataset = train_data, # 使用哪个数据集
    batch_size = batchSize,
    shuffle = True,
    num_workers = 2 # 使用两个进程

)

print("train_loader中的batch数量为:",len(train_loader))