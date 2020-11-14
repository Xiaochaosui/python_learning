import collections
import os
def getAllDirQue(path):
    Queue = collections.deque() # 创建队列
    Queue.append(path)  # 参数path入队
    while len(Queue) != 0: # 空队列结束循环
        dirPath = Queue.popleft() # 弹出第一个
        filesList = os.listdir(dirPath) # 查看dirPath下的所有文件
        for fileName in filesList:  # 挨个遍历dirPath下的所有文件
            fileAbsPath = os.path.join(dirPath,fileName) # 将每个文件合成绝对路径
            if os.path.isdir(fileAbsPath): # 判断是否为目录
                print("目录：",fileName)
                Queue.append(fileAbsPath) # 将目录入队
            else:
                print("普通文件：",fileName)






getAllDirQue(r"G:\py\learning\语音")