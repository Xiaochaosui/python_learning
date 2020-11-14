
class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0
    def run(self):
        print("run")
    def eat(self,food):
        print("eat" + food)

'''
实例化对象
格式：
对象名 = 类名(参数列表)
注意：没有参数，小括号也不能省略

'''
# 实例化对象
per1 = Person()
print(per1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(id(per2))