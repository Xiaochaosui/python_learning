'''
概念：一种保存数据的格式
作用：可以保存的json文件，可以将json串进行传输，通常将json称为轻量级的传输方式

json文件组成：
{}   代表对象(字典)
[]   代表列表
:    代表键值对
,      分隔两个部分

'''
import json
import os
jsonStr = '{"name":"xcs穗","age":18,"hobby":["money","power","pange"]}'

# 将json格式字符串转换成python数据类型的对象
jsonData = json.loads(jsonStr)
# print(jsonData)
# print(type(jsonData))
# print(jsonData["hobby"])

# 将python数据类型的对象转为json格式的字符串
jsonData2 = {"name":"xcs穗","age":18,"hobby":["money","power","pange"]}
jsonStr2 = json.dumps(jsonData2)
# print(jsonStr2)
# print(type(jsonStr2))

# 读取本地的json文件
path1 = os.path.join(os.getcwd()+r"\file","hospital.json")
with open(path1,"rb") as f:
    data = json.load(f) # 不加s 就是读本地的
    #print(data)
    #print(type(data)) # 直接转成字典类型，即python数据类型
# 写本地json
path2 = os.path.join(os.getcwd()+r"\file","test.json")

jsonData3 = [{"name":"xcs穗","age":18,"hobby":["money","power","pange"]}]

with open(path2,"w") as f:
    json.dump(jsonData3,f)

