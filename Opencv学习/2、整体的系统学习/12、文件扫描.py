# author: "xiaochaosui"
# time: '2021/1/22 13:22'
# mail: '939103485@qq.com'
import cv2
from tools import stackImages
import numpy as np
def preProcess(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((7,7),np.int32)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,150,200)
    imgDial = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDial,kernel,iterations=1)
    return imgDial


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        area = cv2.contourArea(cont)
        if area >5000:
            cv2.drawContours(imgContours, cont, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cont, True)
            approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
            print('approx',approx)

cap = cv2.VideoCapture(0)
if cap.isOpened():
    sucess, frame = cap.read()
    while True:
        sucess, frame = cap.read()
        if sucess == True:
            img = frame.copy()
            imgContours = img.copy()
            imgCanny = preProcess(img)
            getContours(imgCanny)
            imgArray = ([img,imgCanny],
                        [img,imgContours])
            imgRes = stackImages(0.6,imgArray)
            cv2.imshow('img',imgRes)
        if cv2.waitKey(1) & 0xFF == 27:
            break

