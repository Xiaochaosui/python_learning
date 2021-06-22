import urllib.request
import os
import re
import ssl
def imageCrawler(url,filePath):
    headrstr = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    htmlPath = os.path.join(os.getcwd(),"htmlStr.html")
    req = urllib.request.Request(url)
    req.add_header("User-Agent",headrstr)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    htmlStr = response.read().decode("utf-8")

    '''with open(htmlPath,"w",encoding="utf-8") as f:
        f.write(htmlStr)'''

    pat = r'<div class="p-img">(.*?)</div>'
    #print(htmlStr)
    re_imageList = re.compile(pat,re.DOTALL)
    imageList = re_imageList.findall(htmlStr)
    #print(imageList[0])
    #print(imageList[1])
    print(len(imageList))
    num = 0
    for con in imageList:
        #print(con)
        # http://img11.360buyimg.com/n1/jfs/t1/148534/18/14934/164250/5fb49cc3E83b66097/eb751745a28bebea.jpg
        pat1 = r'data-lazy-img="//(.*?)"'
        re_image = re.compile(pat1,re.DOTALL)
        image = re_image.findall(con)
        #print(image[0])
        fileName = os.path.join(filePath,str(num)+".jpg")
        num += 1
        # 将图片下载到本地
        if image:
            urllib.request.urlretrieve("http://"+image[0],fileName)
        #print(image)





if __name__ == '__main__':
    url = r"https://search.jd.com/search?keyword=nike&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=nike&ev=exbrand_%E8%80%90%E5%85%8B%EF%BC%88NIKE%EF%BC%89%5E&cid3=9757#J_searchWrap"
    fileDir = os.getcwd()
    if not os.path.exists("image"):
        os.mkdir("image")
    filePath = os.path.join(fileDir,"image")
    imageCrawler(url,filePath)

