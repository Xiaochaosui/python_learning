import torch
from torch.autograd import Variable


# 通过继承
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
    def forward(self,input,w1,w2):
        x = torch.mm(input,w1)
        x = torch.clamp(x,min=0)
        x = torch.mm(x,w2)
        return x
    def backward(self):
        pass


if __name__ == '__main__':
    model = Model()
    # 变量参数
    batch_n = 64
    hidden_layer = 100
    input_data = 1000
    output_data = 10
    # 超参数
    epoch_n = 30
    learning_rate = 1e-6
    # 数据生成
    x = Variable(torch.randn(batch_n, input_data), requires_grad=False)
    y = Variable(torch.randn(batch_n, output_data), requires_grad=False)

    w1 = Variable(torch.randn(input_data, hidden_layer), requires_grad=True)
    w2 = Variable(torch.randn(hidden_layer, output_data), requires_grad=True)

    for epoch in range(epoch_n):
        y_pred = model.forward(x,w1,w2)
        loss = (y_pred - y).pow(2).sum()
        print('Epoch:{},Loss:{:.4f}'.format(epoch + 1, loss))
        loss.backward()

        w1.data -= learning_rate * w1.grad.data
        w2.data -= learning_rate * w2.grad.data  # 更新w1,w2

        w2.grad.data.zero_()
        w1.grad.data.zero_()