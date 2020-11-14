import os

def getAllDirDe(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        #从栈里取数据
        dirPath = stack.pop()
        #print(dirPath)
        filesList = os.listdir(dirPath)
        #print(filesList)
        # 处理每一个文件
        for fileName in filesList:
           fileAbsPath = os.path.join(dirPath,fileName)
           if os.path.isdir(fileAbsPath):
               # 是目录就压栈
               print("目录：", fileName)
               stack.append(fileAbsPath)
           else:
               print("普通文件：", fileName)




getAllDirDe(r"G:\py\learning\语音")