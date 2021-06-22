# author: "xiaochaosui"
# time: '2020/12/19 16:46'
# mail: '939103485@qq.com'
import cv2
import matplotlib as plt
import numpy as np
'''
x轴 正 东 宽度 w
y轴 正 南 高度 h
'''
# 改变图片的size
img = cv2.imread('xiaochaosui.jpg')
print(img.shape)

imgResize = cv2.resize(img,(1500,1400))
print(imgResize.shape)
# 裁剪图片
# 前一个 0：200 是高度H，后面200：500 是w
imgCropped = img[0:200,100:500]
cv2.imshow('imgGray',img)
cv2.imshow('imgResize',imgResize)
cv2.imshow('imgCropped',imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()


