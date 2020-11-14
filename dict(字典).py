'''
概述：
键值存储（key-value） 具有极快的查找速度
key的特性：
1.字典中的key必须唯一
2.key必须是不可变对象
3.字符串、整数都是不可变的，可以作为key
4.list可变的，不能作为key（字符串作为key）
5.存储时无序的
'''

dict1 = {"tom":60,"lilei":70}

# 元素的访问
# 获取：字典名[key]
print(dict1["lilei"])
# print(dict1["xcs"]) 没有

print(dict1.get("xcs"))
ret = dict1.get("xcs")
if ret == None:
    print("没有")
else:
    print("有")

# 添加
dict1["hanmeimei"] = 99
# 修改 覆盖
dict1["lilei"] = 80
print(dict1)
# 删除
dict1.pop("tom")
print(dict1)


# 遍历
for key in dict1:
    print("key=",key,dict1[key])

print("****")
print(dict1.values())
for value in dict1.values():
    print(value)

print(dict1.items())
for k,v in dict1.items():
    print(k,v)

for i,v2 in enumerate(dict1):
    print(i,v2) # 往里存的顺序


# 和list比较
# 1、dict查找和插入的速度极快，不会随着key-value的增加而变慢
# 2、dict需要占用内存，内存浪费多
# 3、list查找和插入速度会随着数据量的增多而减慢，但占用空间小，浪费内存小

w = "good"
str = "xcs 1s a good man! xcs is a good man! xcs is a good man!"

print(str.count(w))

# 练习
d = {}
l = str.split(" ")
print(l)

for v in l:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1

print(d[w])
print(d)

'''
1、以空格切割字符串
2、循环处理列表中的元素
3、以元素当作key去一个字典中提取数据
4、如果没有就以该元素作为key，1作为value存进字典
5、如果提取到就+1
6、根据输入的字符串当多key再去字典取value
'''



