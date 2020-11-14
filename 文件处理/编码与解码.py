
# 编码
path = r"G:\py\learning\文件处理\a2.txt"

with open(path,"wb") as f1:
    str = "xcs穗 is a good man穗"
    f1.write(str.encode("utf-8"))

with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))

