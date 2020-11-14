class Person(object):
    def run(self):
        print("run")
        print(self.__age)
    def eat(self,food):
        print("eat" , food)
    def __init__(self,name,age,height,weight):
        self.name = name
        self.__age = age # 私有属性
        self.height = height
        self.weight = weight
    # 通过内部方法来访问限制属性 赋值和取值
    def setAge(self,age):
        if age < 0:
            age =0
        self.__age = age
    def getAge(self):
        return self.__age

per = Person("tom",20,180,80)
# per.age = 10
# print(per.age) # 外部使用
# per.run() # 内部使用
print(per.getAge())
# 如果要让内部的属性，不被外部直接访问,在属性前加两个下划线__
# 在python 中如果在属性前加两个下划线_，那么这个属性就变成了private

# 在python中__xxx__ 属于特殊变量，可以直接访问

# 在python中_xxx，也可以直接访问，但是按照约定的规则，当我们看到这样的变量
# 时，意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我”
