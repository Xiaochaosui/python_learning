import cv2
import matplotlib as plt
import numpy as np
'''
cv2.IMREAD_COLOR 彩色图像
cv2.IMREAD_GRAYSCALE 灰度图像
'''



img = cv2.imread('xiaochaosui.jpg')
print('img-',img.shape)
kernel = np.ones((3,3),np.uint8)
# 将BGR转换成灰度图
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print('Gray',imgGray.shape)
# 将灰度图 高斯模糊 机密内核大小必须是奇数
imgBlur = cv2.GaussianBlur(imgGray,(99,99),0)
# 边缘检测 线条 ，参数越大显示的 线条越少
imgCanny = cv2.Canny(img,150,200)
# 放大线条，由后面的迭代参数决定，膨胀
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# 侵蚀图片 还原
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow('imgGray',imgGray)
cv2.imshow('imgBlur',imgBlur)
cv2.imshow('imgCanny',imgCanny)
cv2.imshow('imgDialation',imgDialation)
cv2.imshow('imgEroded',imgEroded)
# img1 = cv2.imread('xiaochaosui.jpg',cv2.IMREAD_GRAYSCALE) # 读取是 BGR的
# print(img)
# print(img1)
# # 显示图片
# cv2.imshow('image_xcs',img)
# # 等待时间，毫秒单位，0表示按任意键结束
cv2.waitKey(0)
cv2.destroyAllWindows()

# def cv_show(name,img):
#     cv2.imshow(name,img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# print(img.shape)
# print(img1.shape)

# 保存
#  cv2.imwrite('xcs.jpg',img1)

# 数据读取视频

# 其中参数为0 则为调用摄像头
# vc = cv2.VideoCapture('test.mp4')
#
# # 检查是否正确打开
# if vc.isOpened():
#     open,frame = vc.read()
# else:
#     open = False
#
# while open:
#     ret,frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('res',gray)
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
# vc.release()
# cv2.destroyAllWindows()