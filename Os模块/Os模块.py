import os
'''
Os:包含了普遍的操作系统功能
'''

# 获取操作系统类型 nt-->windows posix-->Linux,Unix或Mac Os X
# print(os.name)
# 打印操作系统详细的信息，windows不支持
# print(os.uname())

# 获取操作系统中的环境变量
# print(os.environ)
# 获取指定环境变量
# print(os.environ.get("PYTHONPATH"))

# 获取当前目录 .
# print(os.curdir)
# 获取当前工作目录，即当前python脚本所在的目录
# print(os.getcwd())

# 以列表形式返回指定目录下的所有文件
# print(os.listdir(r"G:\py\learning\文件处理"))

# 当前目录下创建新目录
# os.mkdir("acs")
# 删除目录
# os.rmdir(r"G:\py\learning\xcs")
# 获取文件属性
# print(os.stat("xcs"))
# 重命名
# os.rename("xcs","xiao")
# 删除普通文件
# os.remove("a.txt")
# 运行shell命令
# os.system("notepad") # 记事本
# os.system("write")  # 写字板
# os.system("mspaint") # 画板
# os.system("msconfig")  # 系统设置
# os.system("shutdown -s -t 500") # 注销
# os.system("shutdown -a") # 取消注销
# os.system("notepad")
# os.system("task kill /f /im notepad.exe")

# 有些方法存在os模块里，还有些存在于os.path
# 查看当前的绝对路径
print(os.path.abspath("./xiao"))


# 拼接路径
p1 = r"G:\py\learning\Os模块"
p2 = r"xiao\a\b"
# pay attention:参数2开始不要有斜杠\
#print(os.path.join(p1,p2))

# 拆分路径
p3 = r"G:\py\learning\Os模块\Os模块.py"
#print(os.path.split(p3))
# 获取扩展名
#print(os.path.splitext(p3))

# 判断是否是目录
#print(os.path.isdir(p3))
# 判断文件是否存在
#print(os.path.isfile(p3))
# 判断目录是否存在
# print(os.path.exists(p1))

# 获得文件大小 字节
#print(os.path.getsize(p3))
# 文件的目录
# print(os.path.dirname(p3))
# print(os.path.basename(p3))