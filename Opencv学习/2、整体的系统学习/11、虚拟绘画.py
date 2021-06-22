# author: "xiaochaosui"
# time: '2021/1/21 10:13'
# mail: '939103485@qq.com'
import cv2
import numpy as np
mypoints = []
points = []
def drawCanvas(points,imgContours):
    for p in points:
        cv2.circle(imgContours, (p[0],p[1]), 10, (255, 0, 0), cv2.FILLED)

def openCamera():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        open,frame = cap.read()
    else:
        open = False
    while open:
        ret, frame = cap.read()
        if frame is None:
            break
        if ret == True:
            #cv2.imshow('img', frame)
            img = frame
            imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            lowerb = np.array([107, 93, 21])
            upperb = np.array([141, 246, 255])
            imgContours = img.copy()
            mask = cv2.inRange(imgHSV,lowerb,upperb)
            x,y = getContours(mask,imgContours)
            #cv2.imshow('mask', mask)

            if x!=0 and y!= 0:
                points.append([x,y])
            drawCanvas(points,imgContours)
            cv2.imshow('res',imgContours)
            if cv2.waitKey(5) & 0xFF == 27:
                break

def getContours(img,imgContours):
    # 从图片中找出所有的轮廓
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    x,y,w,h = 0,0,0,0
    for cnt in contours:
        # 计算面积
        area = cv2.contourArea(cnt)
        if area > 500:
            # 描出轮廓
            cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 2)
            # 这里用True 是为了表示这个 cnt 是封闭的 即闭环
            # 求周长
            peri = cv2.arcLength(cnt,True)

            # 求顶点 第二个参数是分辨率 返回的是顶点的坐标
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objCnt = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

if __name__ == '__main__':
    openCamera()