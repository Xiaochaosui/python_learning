import torch
from torch.autograd import Variable
# 变量参数
batch_n = 100
hidden_layer = 100
input_data = 1000
output_data = 10

#超参数
epoch_n = 20
learning_rate = 1e-6

# 数据生成
x = Variable(torch.randn(batch_n,input_data),requires_grad=False)
y = Variable(torch.randn(batch_n,output_data),requires_grad=False)

w1 = Variable(torch.randn(input_data,hidden_layer),requires_grad=True)
w2 = Variable(torch.randn(hidden_layer,output_data),requires_grad=True)

for epoch in range(epoch_n):
    # 前向传播
    h1 = x.mm(w1)
    h1 = h1.clamp(min=0) #除去 hidden层 小于0的 数据
    y_pred = h1.mm(w2)
    loss = (y_pred-y).pow(2).sum()
    print('Epoch:{},Loss:{:.4f}'.format(epoch+1,loss))
    # 后向传播
    loss.backward()

    w1.data -= learning_rate*w1.grad.data
    w2.data-= learning_rate*w2.grad.data # 更新w1,w2

    w2.grad.data.zero_()
    w1.grad.data.zero_()
