import os
import xlwt
def getFileName(path):
    fileNames = []
    lists = os.listdir(path)
    for fileName1 in lists:
        fileName = fileName1.replace(".pdf","")
        fileNames.append(fileName)
    return fileNames
def wirteFile(path,lists):
    f = open(path, "a",encoding="utf-8")
    for fn in lists:
        f.write(fn+"\n")
if __name__ == '__main__':
    path1 = r"C:\Users\Administrator\Desktop\论文\Extraction"
    path2 = r"C:\Users\Administrator\Desktop\论文\a.txt"
    fileNames = getFileName(path1)
    print(fileNames)
    wirteFile(path2, fileNames)
