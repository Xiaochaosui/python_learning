# 集合
'''
set:类似dict，是一组key 键的集合，不存储value 值
本质：无序和无重复元素的集合
'''

# 创建
# 需要一个set 或 tuple 或dict 或 list 作为输入集合
l = []
t =()
d = {}
s1 = set([3,2,4,1,1,1,4,56,6,9,8,6,3,5,4,2,525,26])
print(s1)
s2 = set((1,2,4,1,1,1,4))
print(s2)
s3 = set({1:"good",2:"nice"})
print(s3)
s4 = set(())
print(s4)
for i in s1:
    print(i)
