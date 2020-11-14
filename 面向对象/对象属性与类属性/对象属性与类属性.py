
class Person(object):
   # 这里的属性实际上是属于类属性，用类名来调用
    name = "person"
    def __init__(self,name):
        # 对象属性
        self.name = name



print(Person.name)
per = Person("tom")
# 对象属性的优先级是高于类属性的
print(per.name)
# 动态的给对象添加对象属性 只针对当前对象生效
per.age = 18
per2 = Person("lilie")
# print(per2.age) # 没有age属性
print(Person.name)

# 删除对象中的name属性，在调用会使用到同名的类属性
del per.name
print(per.name)
# 注意：不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性
# 当删除对象属性后，再使用又能使用类属性了