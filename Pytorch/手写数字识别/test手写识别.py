#import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision
import torchvision.datasets as normal_datasets
import torchvision.transforms as transforms
from torch.autograd import Variable
import cv2

from PIL import Image


# 模型搭建和参数优化
# 在顺利完成数据装载后，我们可以开始编写卷积神经网络模型的搭建和参数优化的代码
# 卷积层使用torch.nn.Conv2d类来搭建
# 激活层使用torch.nn.ReLU 类方法来搭建
# 池化层使用torch.nn.MaxPool2d类方法来搭建
# 全连接层使用 torch.nn.Linear 类方法来搭建

def get_variable(x):
    x = Variable(x)
    return x.cuda() if torch.cuda.is_available() else x

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # 使用序列工具快速构建
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.fc = nn.Linear(7 * 7 * 32, 10)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = out.view(out.size(0), -1)  # reshape
        out = self.fc(out)
        return out


model = torch.load("cnn.pkl")


if torch.cuda.is_available():
    model.cuda()
batch_size = 1

test_dataset = normal_datasets.MNIST(root='./mnist/',
                                     train=False,
                                     transform=transforms.ToTensor())
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=True)
loader = torchvision.transforms.Compose([

torchvision.transforms.ToTensor()])

def image_loader(image_name):

    image = Image.open(image_name).convert('RGB')
    image = loader(image).unsqueeze(0)

    return image.to(torch.float)

X_test, y_test = next(iter(test_loader))

'''imageFileName = "./data/8.png"
img_tensor = image_loader(imageFileName)
X_test =img_tensor
print(img_tensor.size())'''
#print(X_test.size())

inputs = Variable(X_test)
pred = model(inputs)
_, pred = torch.max(pred, 1)


print("Predict Label is:", [i for i in pred])
#print("Real Label is :", [i for i in y_test])

img = torchvision.utils.make_grid(X_test)
img = img.numpy().transpose(1, 2, 0)

std = [0.5, 0.5, 0.5]
mean = [0.5, 0.5, 0.5]
img = img * std + mean
cv2.imshow('win', img)
key_pressed = cv2.waitKey(0)