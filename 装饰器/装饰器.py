'''
概念： 是一个闭包，把一个函数当做参数返回一个替代版的函数
       本质是是一个返回函数的函数
'''


# 简单的装饰器
'''def func1():
    print("xcs is a good man")'''




# f是函数func1的加强版本，装饰之后的
# f = outer(func1)

# 复杂装饰器


'''def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner'''
def outer(func):
    def inner(*args, **kwargs):
        print("************")
        func(*args, **kwargs)
    return inner
# 使用@符号将装饰器应用到函数 @ python2.4支持

@outer
def say(age):
    print("xcs is %d years old"%(age))

say(1)

# 装饰器 不能修改函数的内部 就可以用装饰器去加功能

# 通用装饰器


