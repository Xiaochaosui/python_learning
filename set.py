'''
set:类似dict，是一组key的集合，不存储value
本质：无序和无重复元素的集合
'''

# 创建
# 需要一个set 或 tuple 或dict 作为输入集合
s1 = set([1,2,3,1,1,1,4])
print(s1)
s2 = set((1,2,3,1,1,1,4))
print(s2)
s3 = set({1:"good",2:"nice"})
print(s3)

# 添加 list，dict 不能添加为元素 因为set 不能存可变对象
s4 = set([1,2,3,4])
s4.add(5)
s4.add((6,7))
print(s4)

# 插入整个list dict tuple 字符串 打碎插入 就将其元素插入
s4.update([8,9])
print(s4)


# 删除 直接删那个数 没有下标 因为set是无序的
s5 = set([1,2,3,4])
s5.remove(3)
print(s5)

# 遍历 打印也是无序的
s6 = set("[1,2,3,4]")
for i in s6:
    print(i)

# set 是没有索引的即没有下标 s6[3] 是不合法的

for index,data in enumerate(s6):
    print(index,data)
# 不能有重复的数据 可以用于数据过滤

s7 = set([1,2,3])
s8 = set([2,3,4])
#交集
a1 = s7 & s8
print(a1)
#并集
a2 = s7 | s8
print(a2)
print(type(a2))



