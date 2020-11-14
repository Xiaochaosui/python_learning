import torch
import torch.nn
from torch.autograd import Variable
# 变量参数
batch_n = 64
hidden_layer = 100
input_data = 1000
output_data = 10
# 超参数
epoch_n = 10000
learning_rate = 1e-6
# 数据生成
x = Variable(torch.randn(batch_n, input_data), requires_grad=False)
y = Variable(torch.randn(batch_n, output_data), requires_grad=False)
# torch.nn.Sequential 一种序列容器
#创建模型
# torch.nn.linner 用于定义模型的线性层 完成不同层之间的线性变换
# 参数分别为：输入特征数，输出特征数，是否使用偏置(默认为True)
# 会自动生成对应维度的权重参数与偏置

# torch.nn.ReLU 属于非线性激活类，无参
'''
models = torch.nn.Sequential(
    torch.nn.Linear(input_data,hidden_layer),
    torch.nn.ReLU(),
    torch.nn.Linear(hidden_layer,output_data)
)'''
#print(models)

#用有序字典 传参搭建模型 orderdict 可用于自定义层
from collections import OrderedDict
models = torch.nn.Sequential(OrderedDict([
    ("Line1",torch.nn.Linear(input_data,hidden_layer)),
    ("Relu1",torch.nn.ReLU()),
    ("Line2",torch.nn.Linear(hidden_layer,output_data))]))
#print(models)
#torch.nn.MSELoss() 用于计算均方误差的类
x1 = Variable(torch.rand(100,100))
y1 = Variable(torch.rand(100,100))
loss_fn = torch.nn.MSELoss()
loss1 = loss_fn(x1,y1)
#print(loss.data)

# torch.nn.L1Loss() 用于计算平均绝对误差的类

# torch.nn.CrossEntropyLoss() 用于计算交叉熵

for epoch in range(epoch_n):
    y_pred = models(x)
    loss = loss_fn(y_pred,y)
    if epoch%1000==0:
        print('Epoch:{},Loss:{:.4f}'.format(epoch + 1, loss))
    models.zero_grad()
    loss.backward()
    for param in models.parameters():
        param.data -=param.grad.data * learning_rate