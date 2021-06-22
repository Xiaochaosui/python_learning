# author: "xiaochaosui"
# time: '2021/3/4 18:47'
# mail: '939103485@qq.com'
'''
归一化处理

在卷积神经网络的卷积层之后总会添加BatchNorm2d进行数据的  归一化处理， 这使得数据在进行Relu之前不会因为数据过大而导致网络性能的不稳定，BatchNorm2d()函数数学原理如下：

BatchNorm2d()内部的参数如下：

1.num_features：一般输入参数为batch_sizenum_featuresheight*width，即为其中特征的数量

2.eps：分母中添加的一个值，目的是为了计算的稳定性，默认为：1e-5

3.momentum：一个用于运行过程中均值和方差的一个估计参数（我的理解是一个稳定系数，类似于SGD中的momentum的系数）

4.affine：当设为true时，会给定可以学习的系数矩阵gamma和beta
'''