
class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0
    def run(self):
        print("run")
    def eat(self,food):
        print("eat" , food)

per = Person()
'''
访问属性：
格式：对象名.属性 = 新值

'''

per.name = "tom"
per.age = 18
per.height = 175
per.weight = 120
print(per.name,per.age,per.height,per.weight)

'''
访问方法：
格式：对象名.方法名（参数列表）
'''
per.run()
per.eat("shit")

