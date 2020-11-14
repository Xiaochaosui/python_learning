

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat" , food)
    def say(self):
        print("Hello,my name is "+self.name)
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __del__(self):
        print("这里是析构函数")



'''
析构函数：__del__()  释放对象时，自动调用

'''
per = Person("xcs",18,170,120)

# 释放对象

# del per
# 对象释放后就不能使用了
# print(per.name)


# 在函数里定义的对象，会在函数结束时自动释放，这样可以用来
# 这样可以减少内存空间的浪费
def func():
    per2 = Person("a",1,1,1)
func()

