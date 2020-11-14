import urllib.request
import ssl
import json
import pickle
import os
def ajaxCrawler(url):
    headStr = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}
    # 向请求体里添加“User-Agent”的两种方式
    req = urllib.request.Request(url,headers=headers)
    #req = urllib.request.Request(url)
    #req.add_header("User-Agent",headStr)
    # 使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData

def writeFile(path,data):
    with open(path,"a",encoding="utf-8") as f:
        f.write(data)
        #json.dump(data,f)




if __name__ == '__main__':
    path = os.path.join(os.path.join(os.getcwd(),"file"),"movie2.json")
    for i in range(1):
        url = r"https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start="+str(i*20)+"&limit=20"
        info = ajaxCrawler(url)
        #print(info)
        data = str(info)+'\n'
        newData = data.replace("True", "'True'")
        newData2 = newData.replace("False", "'False'")
        writeFile(path,newData2)




