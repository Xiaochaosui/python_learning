import urllib.request

import random
url = "http://www.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}

'''# 设置一个请求体
req = urllib.request.Request(url,headers=headers)
# 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)'''

agensList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"
]

agentStr = random.choice(agensList)
req = urllib.request.Request(url)
# 向请求体里添加User-Agent
req.add_header("User-Agent",agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))