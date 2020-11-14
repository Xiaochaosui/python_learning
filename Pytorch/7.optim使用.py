import torch
from torch import nn
from torch import optim
class TestNet(nn.Module):
    def __init__(self):
        super(TestNet, self).__init__()

        #定义隐藏层
        '''torch.nn.Sequential是一个Sequential容器，模块将按照构造函数中传递的顺序添加到模块中。另外，也可以传入一个有序模块'''

        self.hidden = nn.Sequential(nn.Linear(13,10),nn.ReLU())
        # 定义预测回归层
        self.regression = nn.Linear(10,1)
    def forward(self,x):
        x = self.hidden(x)
        output = self.regression(x)
        return  output


testNet = TestNet()
#Optim  使用
# 为testNet中的不同层都定义相同的学习率
optimzer1 = optim.Adam(testNet.parameters(),lr=0.001)

# 为为testNet中的不同层都定义不相同的学习率
'''
列表中的字典，分别对应不同层的 参数设置，'params'关键字是用来指定需要优化的层的权重参数,'lr'用来指定相应层的学习率，而列表外面的那个lr是用来指定除了列表中需要优化的其他层次的学习率
'''
optimzer2 = optim.Adam(
    [{"params":testNet.hidden.parameters(),"lr":0.0001},
     {"params":testNet.regression.parameters(),"lr":0.01}],lr=1e-2
    )
# optimzer.zero_grad() 在损失的反向传播之前对参数梯度进行清空
# optimzer.step()  在损失的反向传播loss ，backward() 方法计算梯度之后，用step()方法进行参数更新

loss_fn = nn.MSELoss()
for input,target in dataset:
    optimzer2.zero_grad() # 梯度清零
    output = testNet(input) # 计算预测值
    loss = loss_fn(output,target) # 计算损失
    loss.backward() # 损失 反向传播
    optimzer2.step()
