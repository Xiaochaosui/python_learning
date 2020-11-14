'''
特点:
1.一旦初始化，不能修改  [和list区分] 元组中的元素不能变
'''

tuple1=(1,2,3,4,5)
print(tuple1[0])
# print(tuple1[5]) 下标越界
print(tuple1[-1]) # -1 下标获取最后一个元素 -2倒数第二个
# print(tuple1[-6]) 下标越界

# 修改元组
'''tuple1[0] = 100
print(tuple1)
'''

# 删除元组
tuple2 = (1,2,3)
del tuple2
# print(tuple2)


# 元组的操作
tuple3 = (1,2,3)
tuple4 = (4,5,6)
tuple5 = tuple3 + tuple4
print(tuple5)

# tuple重复
print(tuple3*3)

# tuple是否在元素中
print(3 in tuple5) # 返回true or false

# 元组的截取
# tuple[开始下标：结束下标]
# 从开始截取到结束下标之前
tuple6 = (1,2,3,4,5,6,7)
print(tuple6[2:5])
print(tuple6[:5])
print(tuple6[2:])

# 二维元组
t1 = ((1,2,3),(4,5,6),(7,8,9))
print(t1[1][1])

# 元组的方法

# len() 返回元组的个数
t2 = (1,2,30,4,5)
print(len(t2))

# max() min() 返回元组的最大最小值
print(max(t2))

# list转换成tuple
list = [1,2,3]
t3 = tuple(list)
print(t3)

# 元组的遍历
for i in (1,2,3,4):
    print(i)

print("**")
tuple7 = (1,)
print(tuple7[0])