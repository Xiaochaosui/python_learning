'''
self代表类的实例而非类

哪个对象调用方法，那么该方法中的self就代表哪个对象

self__class__  代表类名

'''

class Person(object):
    def run(self):
        print("run")
        p = self.__class__("tom",30,150,40)
    def eat(self,food):
        print("eat" , food)
    def say(self):
        print("Hello,my name is "+self.name)
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

per1 = Person("tom",20,180,80)
per1.say()
