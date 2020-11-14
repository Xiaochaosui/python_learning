'''
重写：将函数重写定义写一遍


__str__() : 在调用print打印对象时自动调用，是给用户用的，是一个
描述对象的方法
__repr__() ：给机器用的，在python解释器里面直接用的敲对象名在回车后调用
的方法
注意：没有str时，且有repr，str = repr


'''


class Person(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return "%s--%d--%d--%d"%(self.name,self.age,self.height,self.weight)

per = Person("tom",20,180,80)

print(per.__str__())

# 当一个属性值很多，并且需要打印，重写了__str__()方法