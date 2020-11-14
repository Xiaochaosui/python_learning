# 添加 append直接添加不改变类型,extend合并两个列表
list1 = [1,2,3]
a = [5,6,7]
list1.append(5)
print(list1)
list1.append(a)
print(list1)
list1.extend(a)
print(list1)
# insert(index,obj) 插入具体的位置(索引),位置号是两个元素的后一个元素的位置  index->索引 obj为需要被插入的元素
list2 = [1,2,3]
list2.insert(2,["xcs"])
print(list2)

# count返回元素出现的次数 index返回元素的下标
list3 = [1,1,1,13,3,3]
print(list3.index(1,2,len(list3)))
print(list3.count(1))

# 删除
list4 = ["xcs","good","man",1,2]
# 根据index来删除元素
del list4[3]
print(list4)
# pop 只删除最后一个元素的同时将其返回
t = list4.pop()
print(t)
print(list4)
# remove 根据元素的值来删除
list5 = ["xcs","good","man",1,2]
list5.remove("xcs")
print(list5)

# input:请输入水果名字
# output：有这个水果则输出水果的名字:数量，没有则输出"此水果名字已添加"
