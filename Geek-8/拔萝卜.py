
# input : n,m     n=10 ,m=3
# output: 3 6 9 2 7 1 8 5 10 4
n = int(input("兔妈妈有多少个萝卜:"))
m = int(input("每隔多少个萝卜吃一个:"))
carrots = list(range(1,n+1)) # 存萝卜的列表
print("总共的萝卜",carrots)
# 开始拔萝卜
ca = []
c = 0
# 1 2 3 6
#
# 分类讨论
# 1、n>m
# 2、1<n<=m
# 3、n=1
# 2 5 1 3 4
while len(carrots) >0:
    if len(carrots)>m:
           ca.append(carrots.pop(m-1))
           carrots = carrots[m-1:]+carrots[:m-1]
    if len(carrots) <= m :
            index = (m-1)%len(carrots)
            ca.append(carrots.pop(index))
            carrots = carrots[index:] + carrots[:index]
    if len(carrots)==1:
        ca.append(carrots[0])
        break
print("吃萝卜的顺序：",ca)