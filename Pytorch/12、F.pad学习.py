# author: "xiaochaosui"
# time: '2021/3/4 21:23'
# mail: '939103485@qq.com'

'''
F.pad是pytorch内置的tensor扩充函数，便于对数据集图像或中间层特征进行维度扩充，下面是pytorch官方给出的函数定义。

input
需要扩充的tensor，可以是图像数据，抑或是特征矩阵数据
pad
扩充维度，用于预先定义出某维度上的扩充参数
mode
扩充方法，’constant‘, ‘reflect’ or ‘replicate’三种模式，分别表示常量，反射，复制
value
扩充时指定补充值，但是value只在mode='constant’有效，即使用value填充在扩充出的新维度位置，而在’reflect’和’replicate’模式下，value不可赋值
'''

import torch.nn.functional as F
import torch

torch.nn.functional.pad(input, pad, mode='constant', value=0)
