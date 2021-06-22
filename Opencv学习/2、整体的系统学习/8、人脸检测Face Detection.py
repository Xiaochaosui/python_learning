# author: "xiaochaosui"
# time: '2020/12/23 13:44'
# mail: '939103485@qq.com'
'''

Viola
Jones
1、添加级联
CascadeClassifier ，是Opencv中做人脸检测的时候的一个级联分类器。并且既可以使用Haar，也可以使用LBP特征。

Haar特征是一种反映图像的灰度变化的，像素分模块求差值的一种特征。它分为三类：边缘特征、线性特征、中心特征和对角线特征。用黑白两种矩形框组合成特征模板，在特征模板内用 黑色矩形像素和 减去 白色矩形像素和来表示这个模版的特征值。例如：脸部的一些特征能由矩形模块差值特征简单的描述，如：眼睛要比脸颊颜色要深，鼻梁两侧比鼻梁颜色要深，嘴巴比周围颜色要深等。但矩形特征只对一些简单的图形结构，如边缘、线段较敏感，所以只能描述在特定方向（水平、垂直、对角）上有明显像素模块梯度变化的图像结构。这样就可以进行区分人脸。

void detectMultiScale(
    const Mat& image,                //待检测图像
    CV_OUT vector<Rect>& objects,    //被检测物体的矩形框向量
    double scaleFactor = 1.1,        //前后两次相继的扫描中搜索窗口的比例系数，默认为1.1 即每次搜索窗口扩大10%
    int minNeighbors = 3,            //构成检测目标的相邻矩形的最小个数 如果组成检测目标的小矩形的个数和小于minneighbors - 1 都会被排除
                                     //如果minneighbors为0 则函数不做任何操作就返回所有被检候选矩形框
    int flags = 0,                   //若设置为CV_HAAR_DO_CANNY_PRUNING 函数将会使用Canny边缘检测来排除边缘过多或过少的区域
    Size minSize = Size(),
    Size maxSize = Size()            //最后两个参数用来限制得到的目标区域的范围
);
'''
import cv2
# 加载级联文件
faceCascade = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')
img = cv2.imread('res/pic/1.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,0)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
print(faces)
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()