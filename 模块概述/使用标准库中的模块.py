# 引用模块
import sys
import time
import datetime
print(sys.argv) # 获取命令行参数的列表

# 获取命令行参数的列表
for i in sys.argv:
    print(i)

'''name = sys.argv[1]
age = sys.argv[2]
hoby = sys.argv[3]
print(name,age,hoby)'''

# 自动查找所需模块路径的列表
print(sys.path)