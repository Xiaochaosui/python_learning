import torch
import numpy as np
# 创建一个空张量
# x = torch.empty(5,3)
# print(x)
# 创建一个随机初始化的张量
x1 = torch.rand(5,3)
# print(x1)

# 创建一个0张量,类型为long
x2 = torch.zeros(5,3,dtype=torch.long)
# print(x2)
# 直接从数字创建张量
x3 = torch.tensor([5.5,3])
# print(x3)

# 创建一个单位张量,double
x4 = torch.ones(5,3,dtype=torch.double)
# print(x4)

# 从已有的张量创建相同的维度的新张量，并重新定义类型为float
x5 = torch.randn_like(x4,dtype=torch.float)
#print(x5)

# 打印一个张量的维度
#print(x5.size())

# 将两个张量相加 4中方法
x6 = torch.randn(5,3)
x7 = torch.randn(5,3)
#print(x6)
#print(x7)
#print(x6+x7)
#print(torch.add(x6,x7))
'''res = torch.empty(5,3)
torch.add(x6,x7,out = res)
print(res)'''

'''x7.add_(x6)
print(x7)'''

# 取张量的第一列
x8 = torch.tensor([[-1.2549, -1.7105,-0.5820],
        [-0.4944,  0.7872,  2.6687],
        [ 0.9785,  1.4472, -1.6751],
        [ 1.2227,  0.3064,  0.4867],
        [ 0.5172, -1.4429, -3.2427]])

#print(x8[:,0])

# 将一个张量resize成一个一维张量
x9 = torch.randn(4,4)
x10 = x9.view(16)
#print(x9.size(),x10.size())

x11 = x9.view(2,8)
#print(x9)
#print(x11)
# 从张量中取数字
x12 = torch.randn(1)
#print(x12)
#print(x12.item())

# 将张量+1，np数组会随之而变化
'''a = torch.ones(5)
print(a)
b = a. numpy()
print(b)
a.add_(1)
print(a)
print(b)'''
# 从np数组创建张量
'''a = np.ones(5)
b = torch.from_numpy(a)
print(a)
print(b)
# np数组+1之后，张量也随之变化
np.add(a,1,out =a )
print(a)
print(b)'''

# 张量的自动微分

# 新建一个张量，并设置requires_grad = True
'''x13 = torch.ones(2,2,requires_grad= True)
print(x13)

x14 = x13 + 2
print(x14)
#print(x14.grad_fn)
x15 = x14 * x14 *3
out = x15.mean()
print(x15)
print(out)
#out 进行反向传播
out.backward()
# 打印梯度
print(x13.grad)'''

# 创建一个结果为矢量的计算过程(y = x*2^n)
'''
x = torch.randn(3,requires_grad=True)
print(x)
y = x*2
print(y)
print(y.data.norm()) # 对y中所有元素 求平方和然后开根号
while y.data.norm() < 1000:
    y = y*2
print(y)

# 计算v点处的梯度
v = torch.tensor([0.1,1.0,0.001],dtype=torch.float)
y.backward(v)
print(x.grad)

# 关闭梯度功能

print(x.requires_grad)
print((x**2).requires_grad)
with torch.no_grad():
    print((x**2).requires_grad)
'''
# 方法二
# print(x.requires_grad)
# y = x.detach()
# print(y.requires_grad)
# print(x.eq(y).all())

# .repeat() 创建张量
A = torch.tensor([[-2,3],[-3,3]])
B = -A
#print(torch.where(A>2,A,B))'
#print(A[A>1])
#print(A)
#print(A.repeat(3,2))454

# 生成两个指定序列
A = torch.linspace(0,10,6).reshape(2,3)
B = torch.arange(6).reshape(2,3)
print(A)
print(B)
# torch.cat((A,B),dim = num )将两个张量 按照指定的dim连接 生成新的张量
#print(torch.cat((A,B),dim= 1))
#print(A[:,0:2])
#print(torch.cat((A[:,0:2],A,B),dim= 1))

# torch.stack() 函数 将多个张量按照指定的维度进行拼接,并添加一个维度
#print(torch.stack((A,B),dim = 2))

# torch.chunk() 函数 可以将张量分割为特定数量的块
#print(torch.chunk(A,3,dim=1))

# torch.split() 函数在将张量分割为特定数量的块时，可以指定每个块的大小

#
