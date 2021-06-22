import requests
from lxml import etree
import csv
import re
headers = {
    'Referer': 'https://tousu.sina.com.cn/',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'

}

# fp = open('D://链家房价数据.csv','wt',newline='',encoding='utf8')
# writer = csv.writer(fp)
# writer.writerow(('楼盘名', '地址', '房间格式', '房间面积', '价格', '起价', '优点'))

def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf8')
        else:
            print('1')
            return None

    except:
        print('2')
        return None

def look_xhr(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf8')
        else:
            print('1')
            return None

    except:
        print('2')
        return None
def get_info(html):
    #selector = etree.HTML(html)
    #li_list = selector.xpath( "div[@class='seo_data_list']/a[@class='seo_data_list']/text()")
    pat = r'<a href="//(.*?)</a>'
    # print(htmlStr)
    re_imageList = re.compile(pat, re.DOTALL)
    imageList = re_imageList.findall(html)
    #print(imageList)
    res = []
    for data in imageList:
        # 找时间
        pat_time = r'"time">(.*?)</span>'
        re_time = re.compile(pat_time,re.DOTALL)
        time = re_time.findall(data)
        # 找内容
        pat_content = r'<p>(.*?)</p>'
        re_content = re.compile(pat_content, re.DOTALL)
        content = re_content.findall(data)
        #找投诉对象
        pat_object = r'投诉对象]</span>(.*?)</li>'
        re_object = re.compile(pat_object, re.DOTALL)
        object = re_object.findall(data)
        #找投诉要求
        pat_req = r'投诉要求]</span>(.*?)</li>'
        re_req = re.compile(pat_req, re.DOTALL)
        req = re_req.findall(data)
        r = []
        r.append('时间：'+time[0])
        r.append('投诉内容：'+content[0])
        r.append('投诉对象：'+object[0])
        r.append('投诉要求：'+req[0])
        res.append(r)
        #print(r)
    return res


#     for li in li_list:
#         try:
#             name = li.xpath(
#                 "div[@class='resblock-name']/a[@class='name ']/text()")[0]
#             adress_1 = li.xpath(
#                 "div[@class='resblock-location']/span[1]/text()")[0]
#             adress_2 = li.xpath(
#                 "div[@class='resblock-location']/span[2]/text()")[0]
#             adress_3 = li.xpath("div[@class='resblock-location']/a/text()")[0]
#             adress = adress_1 + '/' + adress_2 + '/' + adress_3
#             how_many_1 = li.xpath("a[@class='resblock-room']/span[1]/text()")[0]
#             how_many_2 = li.xpath("a[@class='resblock-room']/span[2]/text()")
#             if how_many_2:
#                 how_many_1 = how_many_1 + '/' + how_many_2[0]
#             else:
#                 pass
#             minaji = li.xpath("div[@class='resblock-area']/span/text()")[0]
#             price = li.xpath(
#                 "div[@class='resblock-price']/div[@class='main-price']/span[@class='number']/text()")[0]
#             price += '元/平(均价)'
#             qijia = li.xpath(
#                 "div[@class='resblock-price']/div[@class='second']/text()")[0]
#             advantge = li.xpath("div[@class='resblock-tag']//text()")
#             mylist = []
#             for i in advantge:
#                 j = i.strip()
#                 if len(j) == 0:
#                     continue
#                 else:
#                     mylist.append(j)
#             real_advantge = '，'.join(mylist)
#             x = [name, adress, how_many_1, minaji, price, qijia, real_advantge]
#             print(x)
#             writer.writerow(x)
#         except:
#             pass

def writeFile(path,datas):
    fp = open(path, 'a')
    for data in datas:
        for d in data:
            fp.write(d+'\n')
        fp.write("\n")
    fp.close()
if __name__ == '__main__':
    url = 'https://tousu.sina.com.cn/'
    url_xhr = r'https://tousu.sina.com.cn/api/index/feed?ts=1607185777743&rs=3Tim1wwOCNQSuK18&signature=1742f2a1fd003f87f0315cc2d305afd68dbb6227e35992d5f00879166084c660&callback=jQuery111208245159009774539_1607185777706&type=1&page_size=10&page=6&_=1607185777718'
    s ='https://tousu.sina.com.cn/api/index/feed?ts=1607185777743&rs=3Tim1wwOCNQSuK18&signature=cd9d07ab5c409e5bc735e2e0cb69b71d2c4e1d3b7b36602a0be2e1f011515bea&callback=jQuery111208245159009774539_1607185777706&type=1&page_size=10&page=7&_=1607185777719'
    s ='https://tousu.sina.com.cn/api/index/feed?ts=1607185777743&rs=3Tim1wwOCNQSuK18&signature=20cc84b8ddb7307ec69dd72e65035a7ff364eff7c0c4894f1fbbc23c6bcf0777&callback=jQuery111208245159009774539_1607185777706&type=1&page_size=10&page=8&_=1607185777720'
    html = get_html(url)
    path = r'C:\Users\Administrator\Desktop\res.txt'
    res = get_info(html)
    writeFile(path, res)
