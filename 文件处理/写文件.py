import time
'''


'''
# 打开文件
path = r"G:\py\learning\文件处理\a1.txt"
f = open(path,"a")
# 写文件
# 1、将信息写入缓冲区
f.write("xcs is a beautiful man穗")

# 2、刷新缓冲区
# 直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新写入
 #不写的话就是 等文件关闭才能刷新

'''
while 1:
    f.write("xcs is a good man\n")
    f.flush()
    time.sleep(0.1)
    f.write("xcs")
'''

#with open(path,"a") as f2:
    #f2.write("good man")
# 关闭文件
f.close()