# author: "xiaochaosui"
# time: '2020/12/23 15:15'
# mail: '939103485@qq.com'

import cv2
import numpy as  np
def faceDetect(img):
    faceCascade = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 0)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

def cameraFaceDetect():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        faceCascade = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')
        open, frame = cap.read()
    else:
        open = False
    while open:
        ret, frame = cap.read()
        if frame is None:
            break
        if ret == True:
            #faceDetect(frame)
            imgFace = frame.copy()
            imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(imgGray, 1.1, 2)
            for (x, y, w, h) in faces:
                cv2.rectangle(imgFace, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(imgFace,'这是你的脸',(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

            cv2.imshow('img', frame)
            cv2.imshow('imgFace', imgFace)
            if cv2.waitKey(1) & 0xFF == 27:
                break
if __name__ == '__main__':
   cameraFaceDetect()