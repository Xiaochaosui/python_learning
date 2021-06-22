import copy,numpy as np

np.random.seed(0)

def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

def sigmoidOutputToDerivative(output):
    return output*(1-output)


# 字典来装 二进制和十进制
int2binary = {}

binary_dim = 8
largest_number = pow(2,binary_dim) # 最大转换为 8 位的二进制数
# unpackbits函数可以把整数转化成2进制数。

binary = np.unpackbits(
    np.array([range(largest_number)],dtype = np.uint8).T,
    axis=1
)
# np.array([range(largest_number)],dtype = np.uint8).T 生成一个[0-255]的 256*1的矩阵
# 然后再 将这个矩阵 的每个数转换成 2进制数的矩阵

for i in range(largest_number):
    int2binary[i] = binary[i]
# key:十进制,V:二进制
# 初始化网络矩阵
alpha = 0.1 # 学习率
input_dim = 2 # 输入的维度
hidden_dim = 16 # 隐藏神经元的个数
output_dim = 1 # 输出的维度

synapse_0 = 2*np.random.random((input_dim,hidden_dim)) -1 # 输出神经元的w0，维度为 2*16
synapse_1 = 2*np.random.random((hidden_dim,output_dim)) -1 # 神经元至输出层的权重w1，
synapse_h = 2*np.random.random((hidden_dim,hidden_dim)) -1

synapse_0_update = np.zeros_like(synapse_0) # 用于存放相应的梯度值
synapse_1_update = np.zeros_like(synapse_1)
synapse_h_update = np.zeros_like(synapse_h)

for j in range(100000):

    a_int = np.random.randint(largest_number/2)
    a = int2binary[a_int]
    b_int = np.random.randint(largest_number / 2)
    b = int2binary[b_int]
    c_int = a_int + b_int
    c = int2binary[c_int]

    d = np.zeros_like(c)  # 预测值

    overallError = 0 # 总的损失
    layer_2_deltas = list()
    layer_1_values = list()
    layer_1_values.append(np.zeros(hidden_dim))

    for position in range(binary_dim):
        # 正向传播
        x = np.array([[a[binary_dim-position-1],b[binary_dim-position-1]]])

        y = np.array([[c[binary_dim-position-1]]]).T
        # 中间两层
        layer1 = sigmoid(np.dot(x,synapse_0)+np.dot(layer_1_values[-1],synapse_h))
        layer2 = sigmoid(np.dot(layer1, synapse_1)) # 即输出值

        layer2_error = y-layer2

        layer_2_deltas.append((layer2_error)*sigmoidOutputToDerivative(layer2))

        overallError += np.abs(layer2_error[0]) # 计算一个十进制数 的总损失

        d[binary_dim-position-1] = np.round(layer2[0][0]) # np.round 方法返回浮点数x的四舍五入值
        layer_1_values.append(copy.deepcopy(layer1)) # 记录每个二进制位的 layer1层的值


    future_layer_1_delta = np.zeros(hidden_dim)
    # 反向传播参数更新
    # 反向传播
    for position in range(binary_dim):
        X = np.array([[a[position],b[position]]])

        layer1 = layer_1_values[-position-1]
        prev_layer1 = layer_1_values[-position-2]
        layer2_delta = layer_2_deltas[-position-1]

        # l1->s_1->l2 所以 l1的误差应该是 两个的相加 循环的误差+输出的误差
        layer1_delta = (future_layer_1_delta.dot(synapse_h.T) + layer2_delta.dot(synapse_1.T)) * sigmoidOutputToDerivative(layer1)
        # 3个权重参数更新
        synapse_1_update += np.atleast_2d(layer1).T.dot(layer2_delta) # np.atleast_2d将输入的数组转换为至少2维
        synapse_h_update += np.atleast_2d(prev_layer1).T.dot(layer1_delta)
        synapse_0_update += X.T.dot(layer1_delta)



        future_layer_1_delta = layer1_delta

    synapse_0 += synapse_0_update * alpha
    synapse_h += synapse_h_update * alpha
    synapse_1 += synapse_1_update * alpha

    synapse_0_update *= 0
    synapse_h_update *= 0
    synapse_1_update *= 0

    if(j%1000==0):
        print("Error:"+str(overallError))
        print("Pred:" + str(d))
        print("True:"+str(c))
        out = 0
        for index,x in enumerate(reversed(d)):
            out += x*pow(2,index)
        print(str(a_int) + "+" +str(b_int)+"="+str(out))
        print("-"*10)







