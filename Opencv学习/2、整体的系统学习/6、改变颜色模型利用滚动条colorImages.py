# author: "xiaochaosui"
# time: '2020/12/20 14:42'
# mail: '939103485@qq.com'
import cv2
import numpy as np
def empty(a):
    pass
img = cv2.imread('xiaochaosui.jpg')
imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow('ControlWindow')
cv2.resizeWindow('ControlWindow',800,400)
cv2.createTrackbar('HueMin','ControlWindow',0,179,empty)
cv2.createTrackbar('HueMax','ControlWindow',179,255,empty)
cv2.createTrackbar('SatMin','ControlWindow',0,179,empty)
cv2.createTrackbar('SatMax','ControlWindow',179,255,empty)
cv2.createTrackbar('ValMin','ControlWindow',0,179,empty)
cv2.createTrackbar('ValMax','ControlWindow',179,255,empty)
while True:
    hueMin = cv2.getTrackbarPos('HueMin','ControlWindow')
    hueMax = cv2.getTrackbarPos('HueMax', 'ControlWindow')
    satMin = cv2.getTrackbarPos('SatMin', 'ControlWindow')
    satMax = cv2.getTrackbarPos('SatMax', 'ControlWindow')
    valMin = cv2.getTrackbarPos('ValMin', 'ControlWindow')
    valMax = cv2.getTrackbarPos('ValMax', 'ControlWindow')
    print(hueMin,hueMax,satMin,satMax,valMin,valMax)
    lowerb = np.array([hueMin,satMin,valMin])
    upperb = np.array([hueMax,satMax,valMax])
    mask = cv2.inRange(imgHsv,lowerb,upperb)
    resultImg  = cv2.bitwise_and(img,img,mask = mask)
    cv2.imshow('img',img)
    cv2.imshow('imgHsv',imgHsv)
    cv2.imshow('mask', mask)
    cv2.imshow('resultImg', resultImg)
    cv2.waitKey(1)
#cv2.destroyAllWindows()