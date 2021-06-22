# author: "xiaochaosui"
# time: '2020/12/20 14:13'
# mail: '939103485@qq.com'
import cv2
import numpy as np
img = cv2.imread('xiaochaosui.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 水平堆叠
imgHor = np.hstack([img,img])
# 垂直堆叠
imgVer = np.vstack([img,img])

cv2.imshow('imgHor',imgHor)
cv2.imshow('imgVer',imgVer)
cv2.waitKey(0)
cv2.destroyAllWindows()