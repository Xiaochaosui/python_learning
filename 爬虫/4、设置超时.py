import urllib.request

# 如果网页长时间未响应，系统判断超时，无法爬取
url = "http://www.baidu.com"
for i in range(1,100):
    try:
        response = urllib.request.urlopen(url, timeout=0.5)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时！")
 