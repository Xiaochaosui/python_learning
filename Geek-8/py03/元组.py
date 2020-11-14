# list []
# tuple ()

list1 = [1,]
t1 = (1,2,3,4,5)
print(list1)
print(t1)
# 通过下标访问元组元素
print(t1[2])
# 与list的区别 tuple不能中途修改
t2 = (1,2,3,4,5)
list2 = [1,2,3,4,5]
list2[4] = 10
print(list2)
# t2[4] = 10
# print(t2)
# 列表之间的连接  注意与extend()的区别
list3 = [1,2,3,4,5]
list4 = [1,2,3,4,5]
print(list3+list4)
list3.extend(list4)
print(list3)
# tuple 之间的连接
t3 = (1,2,3,4,5)
t4 = (1,2,3,4,5)
print(t3[0:0])
