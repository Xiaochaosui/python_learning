from collections.abc import Iterable
from collections.abc import Iterator
'''
可迭代对象：可直接用于for循环的对象(Iterable)
(Iterable) 可以用isinstance()去判断一个对象是否是Iterable对象

可直接用于for循环的数据类型一般分两种
1、集合数据类型，如list，tuple、dict、set、string
2、generator，包括生成器和带yield的generator function

'''
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance(1,Iterable))

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用
并返回下一个值,直到最后抛出一个错误(StopIteration) 表示无法继续返回下一个值

可以被next()函数调用并不断返回下一个值得对象称为迭代器()
(Iterator对象)

可以使用isistance()函数判断一个对象是否为Iterator对象

'''
print("********")
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance(1,Iterator))
print(isinstance((x for x in range(10)),Iterator))

l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

# 转成Iterator对象
a = iter([1,2,3,4])
print(next(a))
print(next(a))

print(isinstance(iter([]),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(""),Iterator))



# 案例
endStr = "end"
str = ""

for line in iter(input,endStr):
    str += line + "\n"
print(str)



