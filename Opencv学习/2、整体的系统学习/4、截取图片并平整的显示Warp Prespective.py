# author: "xiaochaosui"
# time: '2020/12/19 17:24'
# mail: '939103485@qq.com'
import cv2
import numpy as np
img = cv2.imread('res/puke.jpg')
w, h = 250,350
# 原图需要截取下来的图
pts1 = np.float32([[644,67],[964,190],[452,578],[780,693]])
# 生成多大尺寸的图 平整
pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
# 将两个矩阵 透析成一个矩阵 将pts1投影到pts2c
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#
imgOutput = cv2.warpPerspective(img,matrix,(w,h))
cv2.imshow('img',img)
cv2.imshow('imgOutput',imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()