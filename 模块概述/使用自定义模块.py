# 引入模块
# import 语句
# 格式： import module1[,module2][,module3][,...][,moduleN]
# 引入自定义模块，不用加.py后缀
# import xcs
# pay attention:一个模块只会被引入一次，不管执行了多少次import
# 防止模块被多次引入

'''xcs.sayGood()
xcs.sayNice()'''

# from....import 语句
# 作用：从模块中导入一个指定的部分到当面命名空间
# 格式：from module import name

from xcs import sayGood,sayNice

'''
缺点：程序中的函数可以将模块中的同名函数覆盖
def sayGood():
    print("***")'''
# sayGood()
# sayNice()


# from...import *语句
# 作用：把一个模块中所有内容全部导入当前命名空间
from xcs import *

# 最好不要过多使用
'''
缺点：程序中的函数可以将模块中的同名函数覆盖
def sayGood():
    print("***")'''

sayGood()