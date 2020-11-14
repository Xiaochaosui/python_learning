import numpy as np
# 创建数组 用list来传参，如果是一串数字则不予处理(报错)
# a = np.array(1,2,3)  报错
# 一维数组
a = np.array([1,2,3])
#print(a)
# 二维数组
a1 = np.array([[1,2,3],[2,3,5]])
#print(a1)

#创建临时数组

a2 = np.ones([2,3]) #创建一个2*3的全1数组 下标都是从 0，0开始
#print(a2)
a2[1,2] = 2 # 将原有元素覆盖
#print(a2)

# zeros  创建指定维度的全0数组
a3 = np.zeros(16)
#print("*"*10)
#print(a3)

# empty 创建指定维度的 随机数组

a4 = np.empty([2,3])
#print(a4)

# ndim 返回统计的数组维数，即维度的数量(行数),返回一个int
a5 = np.ones([2,3])
#print(a5.ndim)

# shape 返回数组的行列数,返回一个tuple
#print(a5.shape)

# martix 搭建矩阵 ，传参与array一样，不举例子

# size 返回数组或者矩阵的元素总数
#print(a5.size)

# dtype 返回数组中的元素的数据类型，显示的是 numpy中的数据类型
# 如：numpy.int32  numpy.int16 numpy.float64
#print(a1.dtype)
a6 = np.ones([2,3],dtype=np.float64)
#print(a6)
#print(a6.dtype)

# itemsize 返回数组中每个元素的字节大小
# 当dtype = float64 则 itemsize是8 = 64/8
#print(a6.itemsize)

# arange(num) 创建num个元素的一维数组
a7 = np.arange(1000)
#print(a7)

# 数组的运算 同变量运算
# a -b  a+b a*b a/b
x = np.array([1,2,3])
y = np.array([4,5,6])
# dot() 将x,y中各个元素对应相乘 并相加 返回一个标量
z = x.dot(y)
print(z)
z1 = np.dot(x,y)
print(z1)

# min() max() sum()
a8 = np.array([[1,2,3],
               [3,2,1]])

# axis  空参是找整个矩阵，0针对数组的列，1针对数组的行
print("min:",a.min())
print("min:",a.min(axis=0))
print("min:",a.min(axis=1))

# exp()

# sqrt()

# square()

# seed()

# rand() 向上取整

# 整数转换成2进制的函数   unpackbits(myArray,axis=n)
a = np.array([(range(pow(2,8)))], dtype=np.uint8)
b = np.unpackbits(a.T, axis=1)

print("a", a)
print("b", b)