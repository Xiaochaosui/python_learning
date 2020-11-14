import urllib.request
import os

# 想指定的url地址发起请求，并返回服务器响应的数据(文件对象)
response = urllib.request.urlopen("https://jwcnew.webvpn.nefu.edu.cn/dblydx_jsxsd/")

# 读取文件的全部内容，会把读取到的数据赋值到一个字符串变量
data = response.read()#.decode("utf-8")
# print(data)
# print(type(data))

# 将爬取到的网页写入文件
filePath = os.path.join(os.path.join(os.getcwd(),"file"),"file1.html")
with open(filePath,"wb") as f:
    f.write(data)
# 读取一行
'''data1 = response.readlines()
print(data1)
print(type(data1))
print(len(data1))
print(type(data1[100]))'''

# 读取文件的全部内容，会把读取到的数据赋值给一个列表变量

# response 属性
# 返回当前环境的有关信息
# print(response.info())

# 返回状态码 类似404这种 Not Found
#print(response.getcode())
if response.getcode() ==200 or response.getcode() == 304:
    # 处理网页信息
    pass

# 返回当前正在爬取的URL地址
# print(response.geturl())

# 解码
url = r"https://www.baidu.com/s?wd=%E5%B0%8F%E8%8D%89%E7%A9%97&rsv_spt=1&rsv_iqid=0x9d77488f0000480c&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&oq=%25E5%25B0%258F%25E6%259C%259D%25E7%25A9%2597&inputT=2397&rsv_t=2992y2ts3NEa78ZNy%2BCJ2vL4ouFJu1Im%2F%2F20hDqPY4W%2BBlOlysYH6nBPuo4YpRf9z3i9&rsv_pq=a35a96d800001adf&rsv_sug3=29&rsv_sug1=20&rsv_sug7=100&rsv_sug2=0&rsv_sug4=2397"
newUrl = urllib.request.unquote(url)
# print(newUrl)

# 编码
newUrl2 = urllib.request.quote(newUrl)
# print(newUrl2)