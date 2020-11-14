
class Person(object):
    def __init__(self,age):
        # self.age = age
        # 限制访问
        self.__age = age
    '''def getAge(self):
        return self.__age
    def setAge(self,age):
        if age < 0:
            age = 0
        self.__age = age'''
    # 方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    @age.setter # 去掉下划线.setter
    def age(self,age):
        if age < 0:
            age = 0
        self.__age = age



per = Person(18)

# 属性直接对外暴露
# 不安全，没有数据过滤
# per.setAge(19)
# print(per.getAge())
per.age = 100 # 相当于调用setAge()
print(per.age) # 相当于调用getAge()