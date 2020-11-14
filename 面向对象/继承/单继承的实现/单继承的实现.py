from student import Student
from person import Person


per = Person("xcs",13,2)
print(per.getMoney())   # 通过继承过来的公有方法来访问私有属性

stu = Student("tom",18,12345,100)

# print(stu.name,stu.age,stu.stuID)
# stu.stuFunc()
per.setMoney(200)

print(stu.getMoney())
print(per.getMoney())  