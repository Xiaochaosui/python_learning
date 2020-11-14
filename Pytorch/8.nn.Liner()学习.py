import torch
from torch import nn
from torch import autograd
'''
torch.nn.Linear（in_features，out_features，bias = True ）
对传入数据应用线性变换：y = A x+ b
参数：
in_features - 每个输入样本的大小
out_features - 每个输出样本的大小
bias - 如果设置为False，则图层不会学习附加偏差。默认值：True
'''
m = nn.Linear(20, 30) # 20，30指的是维度
input = autograd.Variable(torch.randn(128, 20))
output = m(input)
print(output.size())