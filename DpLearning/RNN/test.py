# author: "xiaochaosui"
# time: '2020/12/18 20:57'
# mail: '939103485@qq.com'

# -*- coding: utf-8 -*-

"""
Created on Mon Sep 24 17:02:41 2018
@author: Abner_hg
"""

import numpy as np
import copy


def sigmoid(x):  # sigmoid
    return 1 / (1 + np.exp(-x))


# convert output of sigmoid function to its derivative   #计算sigmoid函数的倒数
def sigmoid_output_to_derivative(output):  # Sigmoid函数求导
    return output * (1 - output)


binary_dim = 8  # 二进制的长度
int2binary = {}  # 保存数字及其对应的二进制表示

largest_num = pow(2, binary_dim)  # 生成binary_dim所能表示的最大的数字
num_arr = np.array([range(largest_num)], dtype=np.uint8).T  # 生成0到largest之间的所有数字
binary = np.unpackbits(num_arr, axis=1)  # 将对应的数字转为二进制

for i in range(largest_num):  # 保存数字及其对应的二进制
    int2binary[i] = binary[i]

alpha = 0.1  # 学习率
input_dim = 2  # 输入的维度
hidden_dim = 16  # 隐藏层神经元的个数
output_dim = 1  # 输出的维度

W = 2 * np.random.random((input_dim, hidden_dim)) - 1  # 输入至神经元的w0，维度为2X16，取值约束在[-1,1]间
U = 2 * np.random.random((hidden_dim, hidden_dim)) - 1  # 神经元至输出层的权重w1,维度为16X1，取值约束在[-1,1]间
V = 2 * np.random.random(
    (hidden_dim, output_dim)) - 1  # 神经元前一时刻状态至当前状态权重wh,维度为16X16，取值约束在[-1,1]间

W_update = np.zeros_like(W)  # 构造与W相同维度的矩阵，并初始化为全0,用于存放所有时刻产生W的梯度；
U_update = np.zeros_like(U)  # 构造与U相同维度的矩阵，并初始化为全0,用于存放所有时刻产生U的梯度；
V_update = np.zeros_like(V)  # 构造与V相同维度的矩阵，并初始化为全0,用于存放所有时刻产生V的梯度；

for epoch in range(10000):  # 总共迭代10000次
    a_int = np.random.randint(largest_num >> 2)  # 在小于largest_num / 2之中随机挑选一个数字
    a = int2binary[a_int]  # a_int对应的二进制

    b_int = np.random.randint(
        largest_num - a_int)  # 在小于largest_num -a_int之中随机挑选一个数字,之所以这么选取,是为了防止a_int+b_int超出了largest_num，还要重新转化为二进制，没有查字典快，当然，这里也可以修改
    b = int2binary[b_int]  # b_int对应的二进制

    c_int = a_int + b_int
    c = int2binary[c_int]  # c_int对应的二进制

    predict = np.zeros_like(c)  # predict就是预测结果，因此和真正值c的二进制维度是一样的

    total_error = 0  # 总的损失，等价于L
    all_ht_values = list()  # 隐藏层的输出
    all_ht_values.append(np.zeros(hidden_dim))  # 8*16，用于存放所有的ht的值
    delta_zt_values = list()  # 存放所有竖直方向的梯度，即每个时刻损失，对输出层的输入求导

    for pos in range(binary_dim):  # 正向传播，从低位开始计算，也就是从右至左
        # 生成输入和输出
        x = np.array([[a[binary_dim - pos - 1], b[binary_dim - pos - 1]]])  # 每次从a和b的低位各取出1位
        y = np.array([[c[binary_dim - pos - 1]]]).T  # 对应的真实值
        pre_ht = all_ht_values[-1]  # 前一时刻隐藏层的输出，即ht-1
        ht = sigmoid(np.dot(x, W) + np.dot(pre_ht, U))  # 当前时刻隐藏层的输出，即ht

        y_hat = sigmoid(np.dot(ht, V))  # 当前时刻输出层的输出
        predict[binary_dim - pos - 1] = np.round(y_hat[0][0])  # predict预测值

        Lt = y - y_hat  # 每一时刻产生的损失

        delta_zt_values.append((Lt) * sigmoid_output_to_derivative(y_hat))  # 每一时刻都要计算，竖直方向的损失，对输出层的输入的导数
        total_error += np.abs(Lt[0])  # 加入总的损失

        all_ht_values.append(copy.deepcopy(ht))  # 存入当前时刻隐藏层的输出，以便后续需要

    # 到目前为止binary_dim位的二进制已经计算完毕，接下来就是反向传播进行参数更新，BPTT
    # 我们记pre_delta_st = delta_t = delta Lt / delta st，则：
    pre_delta_st = np.zeros(hidden_dim)

    for pos in range(binary_dim):
        X = np.array([[a[pos], b[pos]]])  # 当前时刻，所对应的二进制输入
        ht = all_ht_values[-pos - 1]
        pre_ht = all_ht_values[-pos - 2]

        delta_zt = delta_zt_values[-pos - 1]  # 当前时刻，竖直方向贡献的损失值，这个正向传播的时候已经求出
        # delta L / delta st = (delta L /delta ht)  * (delta ht / delta st)
        #  = [(delta L /delta zt) * (delta zt /delta ht) + (delta L /delta st+1) * (delta st+1 /delta ht)] * (delta ht / delta st)
        #  = [(V.T * delta_zt) + (U.T * delta_st+1)] * sigmoid_output_to_derivative(ht)
        delta_st = (delta_zt.dot(V.T) + pre_delta_st.dot(U.T)) * sigmoid_output_to_derivative(ht)

        V_update += np.atleast_2d(ht).T.dot(delta_zt)  # 计入损失
        W_update += X.T.dot(delta_st)
        U_update += np.atleast_2d(pre_ht).T.dot(delta_st)

        pre_delta_st = delta_st

    W += W_update * alpha
    V += V_update * alpha
    U += U_update * alpha

    W_update *= 0
    V_update *= 0
    U_update *= 0

    # print out progress
    if (epoch % 500 == 0):  # 每500次打印结果

        print("  a_binary:      " + str(a))
        print("+ b_binary:      " + str(b))
        print("--------------------------------")
        print("   Predict:      " + str(predict))

        out = 0
        for index, x in enumerate(reversed(predict)):
            out += x * pow(2, index)
        print("     a + b:      " + str(a_int) + " + " + str(b_int) + " = " + str(out))
        print('\n')
        print(" True_value:   " + str(c))
        print("      Error:   " + str(total_error))

        print('\n')
        print("##################################")
        print("##################################")
        print('\n')