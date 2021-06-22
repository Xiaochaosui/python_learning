# author: "xiaochaosui"
# time: '2020/12/21 14:18'
# mail: '939103485@qq.com'
import cv2
import numpy as np
from tools import stackImages
def getContours(img):
    # 从图片中找出所有的轮廓
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # 计算面积
        area = cv2.contourArea(cnt)
        print('area:',area)

        if area > 500:
            # 描出轮廓
            cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 2)
            # 这里用True 是为了表示这个 cnt 是封闭的 即闭环
            # 求周长
            peri = cv2.arcLength(cnt,True)
            print('peri:',peri)
            # 求顶点 第二个参数是分辨率 返回的是顶点的坐标
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print('approx:',len(approx))
            objCnt = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,0,255),2)
            if objCnt==3:
                objType = 'Tri'
            else:
                objType = 'None'
            cv2.putText(imgContours,objType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)

img = cv2.imread('res/shapes.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,150,200)
imgContours = img.copy()
imgBlank = np.zeros_like(img)

getContours(imgCanny)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgContours,imgBlank]))
cv2.imshow('imgStack',imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows()