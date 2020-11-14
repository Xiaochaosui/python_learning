import urllib.request
import os
import re
import time
def crawler(url):
    headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    req = urllib.request.Request(url)
    req.add_header("User-Agent",headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    return data

def writeData(path,data):
    with open(path,"w",encoding="utf-8") as f:
        f.write(data)

def writeJoke(path,data):
    with open(path,"a",encoding="utf-8") as f:
        f.write(data)


def showData(path,path1):
    with open(path,"r",encoding="utf-8") as f:
        data = f.read()
        p1 = r'<div class="author">(.*?)<div id="qiushi_counts_'
        re_joke = re.compile(p1)
        contentList = re.findall(re_joke,data)
        contentDict = {}
        #print(contentList[0])
        for con in contentList:
            pat1 = r'alt="(.*?)" />'
            pat2 = r'<div class="content" title="2018-11-30">(.*?)</div>'
            re_aut = re.compile(pat1)
            re_content = re.compile(pat2)
            aut = re_aut.findall(con)
            joke = re_content.findall(con)
            #print(aut)
            #print(joke[0])
            contentDict[joke[0]] = aut[0]
        for k,v in contentDict.items():
            str = '@'+v+"  say:"+k+'\n'
            print(str)
            writeJoke(path1,str)
            time.sleep(1)


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), r"file\joke.txt")
    file = os.path.join(os.getcwd(), r"file\joke2.txt")
    for i in range(2,11):
        url = r"http://www.yicommunity.com/30date/index_"+str(i)+".html"
        data = crawler(url)
        writeData(path, data)
        showData(path, file)





