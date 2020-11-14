'''
设计类
类名：见名知意思，首字母大写，其他遵循驼峰原则
属性:见名知意思，遵循驼峰原则
行为(方法/功能):见名知意思，遵循驼峰原则

类：不占内存空间的
格式：
class 类名(父类列表):
       Attribute
       Function
'''
# object ：基类,超嘞，所有类的父类
# 一般没有合适的父类就写object
class Person(object):
    # 定义属性（变量）
    name = ""
    age = 0
    height = 0
    weight = 0
    # 定义方法
    # 注意：方法的参数必须以self当第一个参数
    # self代表类的实例(某个对象)
    def run(self):
        print("run")
    def eat(self,food):
        print("eat" + food)

        


