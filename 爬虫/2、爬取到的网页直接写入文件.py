import urllib.request

urllib.request.urlretrieve(r"http://www.baidu.com", filename=r"G:\py\learning\爬虫\file\file2.html")

# urlretrieve在执行的过程当中，会产生一些缓存

# 清除缓存
urllib.request.urlcleanup()
