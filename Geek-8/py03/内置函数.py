'''# divmod() 取商和余数

t = divmod(20,2)
print(type(t))  # 类型
print(t)

# sum() 求和函数
list1 = [1,2,3,4]
print(sum(list1))
print(sum(list1[2:4]))'''

#70-79 17 27 37 57 47

# 找出1-100里的能被7整除的数或者包含7的数 的个数
'''count = 0
for i in range(1,101):
    if i%7 ==0 or  '7' in str(i):
        print(i,end=" ")
        count += 1
print()
print("总共:",count)'''
#

#   97
# a =
# b =

'''
t = 97
a = t//10
b = 97-a*10
print(a,b)'''
'''count = 0
for i in range(1,101):
    a = i//10
    b = 97-a*10
    if i%7 ==0 or a==7 or b==7 :
        print(i,end=" ")
        count += 1
print()
print("总共:",count)'''

# 1-100以内奇数和
'''t = [i  for i in range(1,101) if i%2!=0]
print(sum(t))'''

#  pow(a,b[,c]) 有返回值 没有c的时候返回a的b次方  有c的话返回的是a的b次方然后对c取余
'''print(pow(2,10))
print(pow(2,10,2))'''
'''
# min() 返回列表最小元素
# max() 返回列表最大元素
list1 = [50,8,9,50,6]
list2 = ['xcs is','good','man']
print(min(list1))
print(max(list1))
print(min(list2))
print(min("fbd","fba","fb"))
'''
# range() 函数 返回一个可迭代对象 类型是 对象

# range(5) [0,1,2,3,4] range(0,5)
#  range(1,5)
t = list(range(1,5)) # 默认间隔长度为1
print(t)
t1= list(range(1,5,2))
print(t1)

list1 = [1,2,3,4]
list1.reverse()
print(list1)

# reversed() 返回一个反转的迭代对象！
list2 = [4,3,2,1]
print(list(reversed(list2)))
# 元组
print(tuple(reversed(list2)))

# slice()  返回的一个切片对象!  与list[start:stop] 对比
s = slice(0,2)
print(list2[s])
print(list2[0:2])
# random   random.randint()  random.choice(list)

# frozenset()  创建一个不可修改的集合  既可以去重又可以防止修改 返回值也是一个可迭代的对象
fs = frozenset([1,2,3])
print(fs)
print(list(fs))

# zip() 压缩 将多个list或者tuple 按索引值相同来压缩成一个元组，各个元组组成一个大的列表
z = zip([1,2,3],[3,2,1])
print(z)
print(list(z))
stuName = ["刘德华","卢本伟","PDD","李云龙"]
stuNo = [202001,202002,202003,202004]
stuAge = [50,30,31,42]
z1 = zip(stuName,stuNo,stuAge)
l1 = list(z1)
print(l1)
print(l1[0][1])

# all()  判断一个iterable(可迭代对象)里所有的元素，如果所有元素都为true，则返回true，否则返回false
# and
# bool
# True   False
# 1       0
# 真      假
list3 = [1,2,3]
print(all(list3))
list4 = [""]
print(all(list4))
# any()      判断一个iterable(可迭代对象)里所有的元素，如果所有元素都为False，则返回False，如果有一个true，否则返回True
# or
# 0 or 1 = 1
# 0 or 0 = 0
# 1 and 1 = 1
# 1 and 0 = 0
# (1 or 0 )and 0 and(0 or 1) = 0
list5 = ["",1,2,3]
print(any(list5))   