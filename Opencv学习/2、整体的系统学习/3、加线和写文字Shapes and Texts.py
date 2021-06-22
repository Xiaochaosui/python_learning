# author: "xiaochaosui"
# time: '2020/12/19 16:59'
# mail: '939103485@qq.com'
import cv2
import numpy as np
#               H    W  C
img = np.zeros((512,512,3),np.uint8)
print(img.shape)
img[:] = 255,0,0
# 创建线条 cv2.line(图片 线条起始位置(w,h) 线条最后位置 线条颜色 线条厚度)
# 参数：  图片 线条起始位置(w,h) 线条最后位置 线条颜色 线条厚度
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
# 创建矩形框 cv2.rectangle(图片 线条起始位置(w,h) 线条最后位置 线条颜色 线条厚度)
# cv2.FILLED 填充
cv2.rectangle(img,(0,0),(200,300),(0,255,0),2)
# 创建圆框
# cv2.circle(图片，圆点坐标，圆半径，颜色，圆边厚度)
cv2.circle(img,(225,150),40,(0,255,255),5)

# 放置功能
# cv2.putText(pic,文字内容，开始位置坐标，文本字体，比例大小，颜色，厚度)
cv2.putText(img,"xcs is a good man!",(100,300),cv2.FONT_ITALIC,1,(0,150,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()