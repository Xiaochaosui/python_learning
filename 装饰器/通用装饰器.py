def outer(func):
    def inner(*args,**kwargs):
        # 添加修改的功能
        print("********")
        func(*args,**kwargs)
    return  inner

@outer
def say(age):
    # 函数的参数理论上是无限制的，但最好不好超过6个
    print(" xcs is %d years old"%(age))


say(18)