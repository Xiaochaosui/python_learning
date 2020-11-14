'''
概念：能处理比定义时更多的参数
'''


# 加了星号*的变量存放所有未命名的变量参数，
# 如果在函数调用时没有指定参数，它就是一个空元组
def func(name,*arr):
    print(name)
    for x in arr:
        print(x)
func("xcs","is")

# ** 代表键值对的参数字典，和*代表的意义类似
def func1(**kwargs):
    print(kwargs)
    print(type(kwargs))
func1(x=1,y=2)

def func2(*args,**kwargs):
    pass

func2()