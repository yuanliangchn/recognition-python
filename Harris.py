# -*- coding: cp936 -*-
import cv2
import numpy as np

#读入图像并转化为float类型，用于传递给harris函数
filename = 'C:/Users/lenovo/Desktop/毕业设计/opencv图片/测试图片/1.jpg'
img = cv2.imread(filename)
 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Show1', gray_img)
print '灰度图像数组：\n %s \n \n' % (gray_img)
'''
print gray_img.shape
print gray_img[:2,:2] #像素
print np.matrix(gray_img)
print int(gray_img.shape[0])
'''
print gray_img.shape
gray_img = np.float32(gray_img) #dtype是float32   数据类型为 float32 的输入图像

#对图像执行harris
Harris_detector = cv2.cornerHarris(gray_img, 2, 3, 0.04)

'''
img - 数据类型为 float32 的输入图像。
blockSize - 角点检测中要考虑的领域大小。
ksize - Sobel 求导中使用的窗口大小
k - Harris 角点检测方程中的自由参数,取值参数为 [0,04,0.06].
'''
#腐蚀harris结果   #这段代码是膨胀　提升后续图像角点标注的清晰准确度　　可有可无　　也可以注释掉
dst = cv2.dilate(Harris_detector, None) #对输入图像用特定结构元素进行膨胀操作，该结构元素确定膨胀操作过程中的邻域的形状，各点像素值将被替换为对应邻域上的最大值
                                        # dst其实就是一个个角度分数R组成,R 也很大,说明这个区域是角点
min_val,max_val,min_indx,max_indx=cv2.minMaxLoc(dst)
print(min_val,max_val,min_indx,max_indx)


# 设置阈值
thres = 0.01*dst.max()
img[dst > thres] = [255,0,0]#标记角点

cv2.imshow('Show', img)
cv2.waitKey()
