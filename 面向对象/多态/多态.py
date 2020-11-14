'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物

'''

from cat import Cat
from mouse import Mouse
from person import Person
if __name__ == '__main__':
    tom = Cat("tom")
    jerry = Mouse("jerry")
    jerry.eat()
    tom.eat()
# 再添加100中动物，也都有name属性和eat方法
# 1、采用继承解决，让所有的类继承一个父类animal
    per = Person()
    #per.feedCat(tom)
    #per.feedMouse(jerry)
    per.feedAnimal(tom)


# 定义一个人类，可以喂猫和老鼠吃东西

# 思考 人要喂100种动物，要写100个feed方法?
