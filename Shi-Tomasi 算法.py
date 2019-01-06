# -*- coding: cp936 -*-
"""
Created on Thu Jun 15 06:43:25 2017
@author: dc
"""
 
import numpy as np
import cv2
#import matplotlib.pyplot as plt
 
#读入图像
filename = 'C:/Users/lenovo/Desktop/毕业设计/opencv图片/测试图片/1.jpg'
img = cv2.imread(filename)

#转化为灰度float32类型进行处理
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = np.float32(img_gray)

#得到角点坐标向量
goodfeatures_corners = cv2.goodFeaturesToTrack(img_gray, 60, 0.01, 10)

goodfeatures_corners = np.int0(goodfeatures_corners) #去除数值后的小数点，成为整数，而不是四舍五入
print(len(goodfeatures_corners))
# 注意学习这种遍历的方法（写法）
for i in goodfeatures_corners:
    
    #注意到i 是以列表为元素的列表，所以需要flatten或者ravel一下。    
    x,y = i.flatten()
 
    cv2.circle(img,(x,y), 5, [0,255,], -1)
     
cv2.imshow('goodfeature',img)
 
cv2.waitKey()
