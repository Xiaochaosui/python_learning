import pickle # 数据持久性模块
'''

'''
path = r"G:\py\learning\文件处理\a4.txt"
myList = (1,2,3)
f = open(path,"wb")
pickle.dump(myList,f)

f.close()

# 读取
with open(path,"rb") as f1:
    tempList = pickle.load(f1)
print(type(tempList))
print(tempList)