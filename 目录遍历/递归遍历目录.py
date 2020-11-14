import os


def getAllDirRe(path,sp = ""):
    #得到当前目录下所有文件
    fileList = os.listdir(path)
    #处理每一个文件
    sp += "  "
    for fileName in fileList:
        # path\filename
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):# 判断是否是目录
           print(sp+"目录：",fileName)
           # 递归调用
           getAllDir(fileAbsPath,sp)
        else:
           print(sp+"文件：",fileName)



getAllDirRe(r"G:\py\learning")