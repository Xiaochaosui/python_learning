'''# 字典
# name1 tel1
# name2 tel2

list1 =[1,2,3,4,5,6]
# 创建字典 {}
dic = {"xcs":"17382865078"}
# 访问  值
print(dic["xcs"])
# 键值对  键:值   key:value
# dic = {key1:value1,key2:value2}
#print(dic["xs"]) 键不存在则报错
dic1 = {"xcs":"17382865078","xs":"1738286508"}
# get() 获得返回值 键不存在不报错
print(dic.get("xcs"))
print(dic.get("xcs1"))
print("***"+dic.get("xcs1","该键值对不存在"))

# 字典的键是唯一的 值不一定是唯一的
# 如果出现重复的键 则 返回字典当中最后一个键对应的值
# 值是可以取任何类型
dic2 = {"xcs":"17382865078","xs":"17382865078","xcs":"173","xcs":"173454**"}
# print(dic2["xcs1"])
print(dic2["xs"])
# 字典的内置函数
# len() 计算字典的元素个数 如果字典当中有重复的键所对应的元素，则所有重复元素只当一个来计算
dic3 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
print(len(dic3))
print(len(dic2))

# dic.keys() 返回字典里所有键组成的 列表
dic4 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
print(dic4.keys())
# dic.values() 返回字典里所有值组成的 列表
dic5 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
print(dic5.values())
# dic.items() 返回字典里所有的键值对
dic6 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
print(dic6.items())
# popitem() 删除字典当中最后一个元素
dic7 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
print(dic7.popitem())
print(dic7)
# update() 函数 把后面那个字典放到前面字典去
# 如果添加的是重复的键 则覆盖原来的值
dic7 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
dic8 = {"xcs3":"17382865078"}
dic7.update(dic8)
print(dic7)
# clear() 删除所有元素 即变成空字典
dic9 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
dic9.clear()
print(dic9)

# 字典的修改
dic10 = {"xcs1":"17382865078","xs":"17382865078","xcs2":"173","xcs3":"173454**"}
# 如果键存在
dic10["xcs1"] = "****"
print(dic10)
# 如果键不存在 则添加此键值对
dic10["asd"] = "////"
print(dic10)
# 删除 del 类比列表
del dic10["xs"]
print(dic10)'''

# 字典遍历 默认遍历的是字典的键
stu = {"001":"刘德华","002":"张学友","003":"郭富城"}
for i in stu:
    print(i,end = " ")
print()
# 方法2
for key in stu.keys():
    print(key, end=" ")
print()
# 遍历字典的值
for i in stu:
    print(stu[i],end = " ")
# 方法2
print()
for v in stu.values():
    print(v, end=" ")
# 遍历字典键值对
print()
for items in stu.items():
    print(items)

# enumerate() 用它来遍历list，tuple或者dict，可以遍历索引和默认遍历时的值    枚举
list1 = ["a","b","c"]
for i,s in enumerate(list1):
    print(i,s)
stu1 = {"001":"刘德华","002":"张学友","003":"郭富城"}
for i,s in enumerate(stu1):
    print(i,s)
for i,s in enumerate(stu1.items()):
    print(i,s)
