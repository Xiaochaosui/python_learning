import os
def work(path):
    resPath =r"G:\py\learning\作业\res"

    # 打开文件
    with open(path,"r",encoding="utf-8") as f:
        while True:
            # xcs@163.com----16565
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            # xcs@163.com
            mailStr = lineInfo.split("----")[0]
            # print(mailStr)
            # 邮箱类型的目录
            try:
                fileType = mailStr.split("@")[1].split(".")[0]
                dirStr = os.path.join(resPath,fileType)
            # print(dirStr)
                if not os.path.exists(dirStr):
                 # 存在,不管
                     os.mkdir(dirStr)
            # 创建文件
                filePath = os.path.join(dirStr,fileType+".txt")
                with open(filePath,"a") as fw:
                     fw.write(mailStr+"\n")
            except:
                pass




def getAllDirDe(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dirPath = stack.pop()
        filesList = os.listdir(dirPath)
        for fileName in filesList:
           fileAbsPath = os.path.join(dirPath,fileName)
           if os.path.isdir(fileAbsPath):
               stack.append(fileAbsPath)
           else:
               work(fileAbsPath)

getAllDirDe(r"G:\py\learning\作业")