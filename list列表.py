'''
创建列表
列表名=[列表项1，列表项2，。。。。]
'''
# 创建的空列表
list1=[]
print(list1)
# 创建带元素的列表
list2=[1,2,3,4]
# pay attention : 列表中元素数据可以不同类型
list3 = [1,2,"xiao","good",True]
print(list3)

# 列表元素的访问
# 取值 格式：list[下标]
print(list2[2])


# 替换  下标元素不要越界
list2[2]=300
print(list2)


# 列表操作

# 列表组合
list4=list2+list3
print(list4)

# list重复
print("list重复",list2*3)

# 判断元素是否在列表中
list5 = [1,2,3,4,8,9]
print(3 in list5)
print(6 in list5)

# 列表截取
print(list5[2:4])
print(list5[2:])
print(list5[:4])

# 二位列表
list6 = [[1,2,3],[11,22,33],[111,222,333]]
print(list6[1][1])

# 列表方法

# append() 在列表末尾添加新的元素
list7=[1,2,3,4,5]
list7.append(6)
list7.append([7,8,9])
print(list7)

# extend() 末尾一次性加另一个列表中的多个值
list7.extend([6,7,8])
print(list7)

# insert(x,y) 在下标x处添加一个元素y，不覆盖原数据
list8 = [1,2,3,4,5]
list8.insert(1,100)
print(list8)

# pop(x) 删除掉下标x 元素，默认最后一个 list[-1]
list8.pop(2)
print(list8)

list9 = [1,2,3,4,5]
print(list9.pop(-1))


# remove(x) 移除列表中的第一个个元素x 只能移除一个
list10 = [1,2,3,4,5,4,2,4,5]
list10.remove(4)
print(list10)

# clear() 清除列表所有数据
list10.clear()
print(list10)

# index(x) 查找列表中x元素的第一个匹配的索引值
list11 = [1,2,3,3,4,5,3]
index11 = list11.index(3,4,7)
print(index11)

# len() 列表中元素个数
list12 = [1,2,3,4,5]
print(len(list12))

# max()  min()  列表中最大、最小元素
print(max(list12))
print(min(list12))

# count() 查看元素在列表中出现的次数
list13 = [1,2,3,4,5,3,3,3,3,3,4,4,4]
print(list13.count(3))

# reverse() 列表倒序
list14 = [1,2,3,4,5]
list14.reverse()
print(list14)

# sort() 升序
list14.sort()
print(list14)

# 拷贝
# 浅拷贝
print("**")
list15 = [1,2,3,4,5]
list16 = list15
print(list15,list16)
list16[2]=100
print(list15,list16)

# 深拷贝
list17 = list15.copy()
print(id(list17))
print(id(list15))

# 将元组转换成列表
list18 = list((1,2,3))
print(list18)
