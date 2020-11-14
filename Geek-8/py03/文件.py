# 文件操作

# 打开文件

# f = open(文件名，访问模式)
# 文件名     ti.txt    相对路径+名字
 #          C:\Users\Administrator\Desktop\File\ti.txt         绝对路径+名字
'''
r  只读方式打开文件 打开文件放在文件的开头
w  只写方式打开文件 有原文件则覆盖,无则新建
a   打开一个文件用于文件末尾追加,文件不存在也可以新建
'''
fileName = r"C:\Users\Administrator\Desktop\f\xcs-20-08-03.txt"
# f = open( r"C:\Users\Administrator\Desktop\File\ti.txt",'r')
f = open(fileName,'r',encoding="utf-8") # encoding 解码 编码格式  "utf-8"
# 读取文件内容 如果'r' 省略则默认打开方式为 只读方式
# read(num) 返回的是读取文件当中前num位字符,相应的指针移动到对应位置， 如果没有num参数，默认读取文件当中的全部内容
# 读num个字符的
#con1 = f.read(10)
#print(con1)
# 读取全部的内容的
#con2  = f.read()
#print(con2)
# 按行读取返回的列表
# readlines() 返回的是一个列表，列表中每个元素由每一行的数据构成
#con3 = f.readlines()
#print(con3)
# 按行输出
# readline() 每次只输出一行 返回的是字符串类型
con4 = f.readline()
print(con4,end="")
con5 = f.readline()
print(con5)

# 写入数据  write()有返回值 返回值是写入的数据长度
#str = "xcs穗 is a good man! 真帅111！"
#content = f.write(str)
#print(content)

# 键盘->内存->硬盘
# 运行内存  存储

#  关闭文件
f.close()


