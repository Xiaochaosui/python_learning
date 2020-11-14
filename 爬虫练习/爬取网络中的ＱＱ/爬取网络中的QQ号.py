import urllib.request
import ssl
import re
import os
import collections


def writeFileBytes(htmlBytes,toPath):
    with open(toPath,"wb") as f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes,toPath):
    with open(toPath, "w",encoding="utf-8") as f:
        f.write(htmlBytes.decode("utf-8"))

def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()

def qqCrawler(url,toPath):
    htmlBytes = getHtmlBytes(url)
    #toPath1 = os.path.join(os.getcwd(),"fileBytes.html")
    #toPath2 = os.path.join(os.getcwd(),"fileStr.txt")
    #writeFileBytes(htmlBytes,toPath1)
    #writeFileStr(htmlBytes,toPath2)
    htmlStr = str(htmlBytes)

    # 找QQ号写入文件
    pat = r' <p class=" reply-content">([1-9]\d{4,9})</p>'
    re_qq = re.compile(pat,re.DOTALL)
    qqsList = re_qq.findall(htmlStr)
    qqsList = list(set(qqsList))
    #print(type(qqsList))
    #print(qqsList)
    with open(toPath,"a") as f:
        for qq in qqsList:
            f.write("QQ:"+qq+"\n")
    print(len(qqsList))

    #爬网址
    pat1 = r'(([hH][tT]{2}[pP]://|[hH][tT]{2}[pP][sS]://|[wW]{3}.|[wW][aA][pP].|[fF][tT][pP].|[fF][iI][lL][eE].)[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])'


    re_url = re.compile(pat1)
    urlsList = re_url.findall(htmlStr)
    #去重
    urlsList = list(set(urlsList))
    return urlsList
    '''for urlList in urlsList:
        print(urlList[0])
    print(len(urlsList))'''


def centerControl(url,toPath):
    queue = collections.deque()
    queue.append(url)
    i=1
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlsList = qqCrawler(targetUrl,toPath)
        with open(toPath, "a") as f:
            f.write("第"+str(i)+"页：" +"\n")
        for urls in urlsList:
            templeUrl = urls[0]
            queue.append(templeUrl)
        i += 1


if __name__ == '__main__':
    url = r"https://www.douban.com/group/topic/110094603/"
    toPath = os.path.join(os.getcwd(),"QQNumber.txt")
    centerControl(url,toPath)
