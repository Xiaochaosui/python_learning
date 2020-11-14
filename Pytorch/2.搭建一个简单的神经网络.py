import torch
# 变量参数
batch_n = 100
hidden_layer = 100
input_data = 1000
output_data = 10

#超参数
epoch_n = 20
learning_rate = 1e-6

# 数据生成
x = torch.randn(batch_n,input_data)
y = torch.randn(batch_n,output_data)

w1 = torch.randn(input_data,hidden_layer)
w2 = torch.randn(hidden_layer,output_data)

for epoch in range(epoch_n):
    # 前向传播
    h1 = x.mm(w1)
    h1 = h1.clamp(min=0) #除去 hidden层 小于0的 数据
    y_pred = h1.mm(w2)
    loss = ((y_pred-y).pow(2).sum()/(y.numel())).sqrt()
    print('Epoch:{},Loss:{:.4f}'.format(epoch+1,loss))
    # 后向传播
    grad_y_pred = 2*(y_pred-y)
    grad_w2 = h1.mm(grad_y_pred) #求w2 参数的导

    grad_h = grad_y_pred.clone()
    grad_h = grad_h.mm(w2.t())
    grad_h = grad_h.clamp(min=0)
    grad_w1 = x.t().mm(grad_h) # 链式法则 w1的变化

    w1 -= learning_rate*grad_w1
    w2 -= learning_rate*grad_w2 # 更新w1,w2
