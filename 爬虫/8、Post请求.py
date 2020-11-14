'''
特点：把参数进行打包，单独传输
优点：数据量大，安全，当对服务器数据进行修改最好用Post

缺点：速度慢

'''

import urllib.request
import urllib.parse

url = r"https://jwcnew.webvpn.nefu.edu.cn/dblydx_jsxsd/"
headers = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
# 将要发送的数据合成一个字典
# 字典的建去网址里找，一般为input下name属性的取值
data = {
    "username":"2016214422",
    "password":"xiao939103485"
}

# 对要发送的数据进行打包
postData = urllib.parse.urlencode(data).encode("utf-8")
# 请求体
req = urllib.request.Request(url, postData)

req.add_header("User-Agent",headers)
# 发起请求
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))