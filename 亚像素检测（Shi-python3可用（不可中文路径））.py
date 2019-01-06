# -*- coding: cp936 -*-
import numpy as np
import cv2
from PIL import Image
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp=np.zeros((6*7,3),np.float32)
objp[:,:2]=np.mgrid[0:7,0:6].T.reshape(-1,2)
objpoints = []
imgpoints = []
filename1 = 'C:/Users/lenovo/Desktop/opencv_pic/1.jpg'
img = cv2.imread(filename1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

#Shi-Tomasi角点检测
corners = cv2.goodFeaturesToTrack(gray_img,100,0.01,10)
#corners = np.int0(corners)#为整数值的像素位置
print(corners)
objpoints.append(objp)
corners = cv2.cornerSubPix(gray_img, corners, (5, 5), (-1, -1), criteria)

#亚像素角点检测
#gray_img = np.float32(gray_img)

corners2 = cv2.cornerSubPix(gray_img, corners, (5, 5), (-1, -1), criteria)
#imgpoints.append(corners2)

for i in corners2:
    #注意到i 是以列表为元素的列表，所以需要flatten或者ravel一下。    
    x,y = i.flatten()
    cv2.circle(img,(x,y), 5, [0,255,], -1)#然后在画圆标记

'''
#x,y = corners()
#cv2.circle(img,(x,y), 5, [0,255,], -1)#然后在画圆标记drawChessboardCorners()
img=cv2.drawChessboardCorners(img,(7,6),corners2,False)
#img[corners2>0.01*corners2.max()] = [255,0,0]#标记角点
'''
print (corners2)

cv2.imshow('goodfeature',img)#显示到图像上

cv2.waitKey(20000)
cv2.destroyAllWindows()
