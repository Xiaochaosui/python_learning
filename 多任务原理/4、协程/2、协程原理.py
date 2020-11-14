'''
Python对协程的支持使通过generator实现的



'''

def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

# 协程的最简单风格，控制函数的阶段执行,节约线程或者进程的切换，返回值是一个生成器


m = run()
print(next(m))
print(next(m))