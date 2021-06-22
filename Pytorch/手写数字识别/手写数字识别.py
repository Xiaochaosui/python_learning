import torch
from torch.autograd import Variable
from torchvision import datasets,transforms
import torchvision
#import matplotlib.pyplot as plt

# 参数
batch_size = 64
learning_rate = 0.001
'''transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5],std = [0.5,0.5,0.5])
])'''
# 数据集下载
data_train = datasets.MNIST(
    root="./data/",
    transform=transforms.ToTensor(),
    train=True,
    download=False
)
data_test = datasets.MNIST(
    root="./data/",
    transform=transforms.ToTensor(),
    train=False
)


# 数据装载
data_loder_train = torch.utils.data.DataLoader(
    dataset = data_train,
    batch_size = batch_size,
    shuffle = True
)
data_loder_test = torch.utils.data.DataLoader(
    dataset = data_test,
    batch_size = batch_size,
    shuffle = True
)
# 数据预览

images,labels = next(iter(data_loder_train))
img = torchvision.utils.make_grid(images)
img = img.numpy().transpose(1,2,0)


std = [0.5,0.5,0.5]
mean = [0.5,0.5,0.5]
img = img*std+mean
print(labels)
# plt.imshow(img)
'''import cv2
cv2.imshow('win',img)
key_pressed = cv2.waitKey(0)'''

# 搭建模型
'''
卷积神经网络CNN的结构一般包含这几层：
 
    输入层：用于数据的输入
 
    卷积层：使用卷积核进行特征提取和特征映射
 
    激励层：由于卷积也是一种线性运算，因此需要增加非线性映射
 
    池化层：进行下采样，对特征图稀疏处理，减少特征信息的损失
 
    输出层：用于输出结果
'''
#模型搭建和参数优化
# 在顺利完成数据装载后，我们可以开始编写卷积神经网络模型的搭建和参数优化的代码
#卷积层使用torch.nn.Conv2d类来搭建
# 激活层使用torch.nn.ReLU 类方法来搭建
# 池化层使用torch.nn.MaxPool2d类方法来搭建
# 全连接层使用 torch.nn.Linear 类方法来搭建
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(1,64,kernel_size=3,stride=1,padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(stride=2,kernel_size=2)
        )

        self.dense = torch.nn.Sequential(
            torch.nn.Linear(14*14*128,1024),
            torch.nn.ReLU(),
            torch.nn.Dropout(p = 0.5),#防止过拟合的函数,原理:以一定概率将参数归零
            torch.nn.Linear(1024,10)
        )

    def forward(self,x):
        x = self.conv1(x)
        x = x.view(-1,14*14*128)
        x = self.dense(x)
        return x


model = Model()
print(model)
    # loss函数 计算熵的
cost = torch.nn.CrossEntropyLoss()
    # 优化函数
optimzer = torch.optim.Adam(model.parameters())

    # 训练模型
epoch_n = 5
    # 训练
for epoch in range(epoch_n):
    running_loss = 0.0
    running_correct = 0
    print("Epoch {}/{}".format(epoch,epoch_n))
    print("-"*10)
    i=0
    for data in data_loder_train:
        x_train,y_train = data
        x_train,y_train = Variable(x_train),Variable(y_train)
            # 前向传播
        outputs = model(x_train)
        _,pred = torch.max(outputs.data,1)
        optimzer.zero_grad()
            # 计算熵(loss函数)
        loss = cost(outputs,y_train)
            # 后向传播
        loss.backward()
        optimzer.step() # 更新网络参数
        scheduler = '' # 设置学习率的调整方式
        scheduler.step() # 更新学习率
        if (i + 1) % 10 == 0:
            print('Epoch [%d/%d], Iter [%d/%d] Loss: %.4f'
                  % (epoch + 1, epoch_n, i + 1, len(data_train) // batch_size, loss.item()))
        running_loss += loss.data
        running_correct += torch.sum(pred == y_train.data)
        i +=1


    testing_correct = 0
        # 测试
    for data in data_loder_test:
        x_test,y_test = data
        x_test,y_test = Variable(x_test),Variable(y_test)
        outputs = model(x_test)
        _,pred = torch.max(outputs.data,1)
        testing_correct += torch.sum(pred == y_test.data)
        print("Loss :{:.4f},Train Acc:{:.4f}%,Test Acc:{:.4f}".format(running_loss/len(data_train),100*running_correct/len(data_train),100*testing_correct/len(data_test)))


