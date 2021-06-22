# author: "xiaochaosui"
# time: '2020/12/23 14:35'
# mail: '939103485@qq.com'
'''
调用摄像头
# cap.set(propId, value)
# 设置视频参数: propId - 设置的视频参数, value - 设置的参数值

# cap.isOpened() 返回 true/false, 检查摄像头初始化是否成功

# cap.read()
"""
返回两个值
    先返回一个布尔值, 如果视频读取正确, 则为 True, 如果错误, 则为 False;
    也可用来判断是否到视频末尾;

    再返回一个值, 为每一帧的图像, 该值是一个三维矩阵;

    通用接收方法为:
        ret,frame = cap.read();
        ret: 布尔值;
        frame: 图像的三维矩阵;
        这样 ret 存储布尔值, frame 存储图像;

        若使用一个变量来接收两个值, 如:
            frame = cap.read()
        则 frame 为一个元组, 原来使用 frame 处需更改为 frame[1]
"""

#cv2.waitKey(1) 读取按键，每帧数据延时 1ms, 延时为0, 读取的是静态帧

#cv2.imwrite("test.jpg", img_camera)保存图像

#释放摄像头 cap.release()
#销毁窗口 cv2.destroyAllWindows()

'''
# 颜色检测
import cv2
import numpy as  np
def empty(a):
    pass
# 创建跟踪条的框
def createTrace():
    cv2.namedWindow('ControlWindow')
    cv2.resizeWindow('ControlWindow', 800, 400)
    cv2.createTrackbar('HueMin', 'ControlWindow', 0, 179, empty)
    cv2.createTrackbar('HueMax', 'ControlWindow', 179, 255, empty)
    cv2.createTrackbar('SatMin', 'ControlWindow', 0, 179, empty)
    cv2.createTrackbar('SatMax', 'ControlWindow', 179, 255, empty)
    cv2.createTrackbar('ValMin', 'ControlWindow', 0, 179, empty)
    cv2.createTrackbar('ValMax', 'ControlWindow', 179, 255, empty)
    hueMin = cv2.getTrackbarPos('HueMin', 'ControlWindow')
    hueMax = cv2.getTrackbarPos('HueMax', 'ControlWindow')
    satMin = cv2.getTrackbarPos('SatMin', 'ControlWindow')
    satMax = cv2.getTrackbarPos('SatMax', 'ControlWindow')
    valMin = cv2.getTrackbarPos('ValMin', 'ControlWindow')
    valMax = cv2.getTrackbarPos('ValMax', 'ControlWindow')
    lowerb = [hueMin,satMin,valMin]
    upperb = [hueMax,satMax,valMax]
    return lowerb,upperb
    #print(hueMin, hueMax, satMin, satMax, valMin, valMax)

myColors = [[0,166,70,255,238,220],
            [133,70,60,243,175,255]]

def detectColor(img,myColors):
    for color in myColors:
        lowerb = np.array(color[0:3])
        upperb = np.array(color[3:6])
        mask = cv2.inRange(img, lowerb, upperb)
        # 在面具上 描出轮廓
        getContours(mask)
        #cv2.imshow('resultImg'+str(color[0]), mask)


def getContours(img):
    # 从图片中找出所有的轮廓
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # 计算面积
        area = cv2.contourArea(cnt)
        if area > 500:
            # 描出轮廓
            cv2.drawContours(imgRes, cnt, -1, (255, 0, 0), 2)
            # 这里用True 是为了表示这个 cnt 是封闭的 即闭环
            # 求周长
            peri = cv2.arcLength(cnt,True)
            # 求顶点 第二个参数是分辨率 返回的是顶点的坐标
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)


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
        imgRes = frame.copy()
        imgHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        detectColor(imgHsv, myColors)
        #resultImg = cv2.bitwise_and(img, img, mask=mask)
        #cv2.imshow('imgHsv', imgHsv)
        cv2.imshow('img', imgRes)
        if cv2.waitKey(1) & 0xFF == 27:
            break





