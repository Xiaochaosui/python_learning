import torch
import torch.nn
from torch.autograd import Variable
from collections import OrderedDict
# 变量参数
batch_n = 100
hidden_layer = 100
input_data = 1000
output_data = 10
# 超参数
epoch_n = 20
learning_rate = 1e-4
# 数据生成
x = Variable(torch.randn(batch_n, input_data), requires_grad=False)
y = Variable(torch.randn(batch_n, output_data), requires_grad=False)


models = torch.nn.Sequential(OrderedDict([
    ("Line1",torch.nn.Linear(input_data,hidden_layer)),
    ("Relu1",torch.nn.ReLU()),
    ("Line2",torch.nn.Linear(hidden_layer,output_data))]))

loss_fn = torch.nn.MSELoss()

# torch.optim.Adam() 是一个优化函数,如果没有输入lr的初始值的话，就默认为0.001，可以自适应调节参数
optimzer = torch.optim.Adam(models.parameters(),lr= learning_rate)
for epoch in range(epoch_n):
    y_pred = models(x)
    loss = loss_fn(y_pred,y)
    print('Epoch:{},Loss:{:.4f}'.format(epoch + 1, loss.data))

    # 模型参数梯度归零
    optimzer.zero_grad()

    loss.backward()

    # 计算得到各个节点的梯度值 并更新
    optimzer.step()