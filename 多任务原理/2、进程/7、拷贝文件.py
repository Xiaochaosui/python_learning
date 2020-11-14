import os,time
from multiprocessing import pool

# 实现文件的拷贝
def copyFile(rPath,wPath):
    fr = open(rPath,"rb")
    fw = open(wPath,"wb")

    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()


if __name__ == '__main__':
    start = time.time()
    path = r'G:\py\learning\多任务原理\2、进程\file'
    toPath =r'G:\py\learning\多任务原理\2、进程\tofile'
# 读取path下的所有文件
fileList = os.listdir(path)
# 启动for循环处理每个文件
for fileName in fileList:
    rPath = os.path.join(path,fileName)
    wPath = os.path.join(toPath,fileName)
    copyFile(rPath,wPath)
end = time.time()
print("总耗时：%.2f"%(end-start))