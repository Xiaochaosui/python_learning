# author: "xiaochaosui"
# time: '2021/1/21 12:26'
# mail: '939103485@qq.com'

import cv2
import numpy as np
def empty(a):
    pass

cv2.namedWindow('ControlWindow')
cv2.resizeWindow('ControlWindow', 800, 400)
cv2.createTrackbar('HueMin', 'ControlWindow', 0, 179, empty)
cv2.createTrackbar('HueMax', 'ControlWindow', 179, 255, empty)
cv2.createTrackbar('SatMin', 'ControlWindow', 0, 179, empty)
cv2.createTrackbar('SatMax', 'ControlWindow', 179, 255, empty)
cv2.createTrackbar('ValMin', 'ControlWindow', 0, 179, empty)
cv2.createTrackbar('ValMax', 'ControlWindow', 179, 255, empty)

cap = cv2.VideoCapture(0)
if cap.isOpened():
    open,frame = cap.read()
else:
    open = False
while open:
    if open == True:
        open, frame = cap.read()
        imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        hueMin = cv2.getTrackbarPos('HueMin', 'ControlWindow')
        hueMax = cv2.getTrackbarPos('HueMax', 'ControlWindow')
        satMin = cv2.getTrackbarPos('SatMin', 'ControlWindow')
        satMax = cv2.getTrackbarPos('SatMax', 'ControlWindow')
        valMin = cv2.getTrackbarPos('ValMin', 'ControlWindow')
        valMax = cv2.getTrackbarPos('ValMax', 'ControlWindow')
        lowerb = np.array([hueMin, satMin, valMin])
        upperb = np.array([hueMax, satMax, valMax])
        # 设置一个HSV参数 用于覆盖到原图上
        mask = cv2.inRange(imgHSV, lowerb, upperb)
        resultImg = cv2.bitwise_and(frame, frame, mask=mask)
        print(lowerb, upperb)
        cv2.imshow('CAP',frame)
        #cv2.imshow('img', imgHSV)
        cv2.imshow('mask', mask)
        #cv2.imshow('res',resultImg)
        if cv2.waitKey(1) & 0xFF == 27:
            break



