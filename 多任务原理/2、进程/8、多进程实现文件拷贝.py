import os,time
from multiprocessing import Pool

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
    toPath = r'G:\py\learning\多任务原理\2、进程\tofile'

    filesList = os.listdir(path)

    pp = Pool(5)
    for fileName in filesList:
        rPath = os.path.join(path, fileName)
        wPath = os.path.join(toPath, fileName)
        pp.apply_async(copyFile,args=(rPath,wPath))

    pp.close()
    pp.join()
    end = time.time()
    print("总耗时：%.2f" % (end - start))