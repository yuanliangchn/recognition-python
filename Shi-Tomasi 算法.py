# -*- coding: cp936 -*-
"""
Created on Thu Jun 15 06:43:25 2017
@author: dc
"""
 
import numpy as np
import cv2
#import matplotlib.pyplot as plt
 
#����ͼ��
filename = 'C:/Users/lenovo/Desktop/��ҵ���/opencvͼƬ/����ͼƬ/1.jpg'
img = cv2.imread(filename)

#ת��Ϊ�Ҷ�float32���ͽ��д���
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = np.float32(img_gray)

#�õ��ǵ���������
goodfeatures_corners = cv2.goodFeaturesToTrack(img_gray, 60, 0.01, 10)

goodfeatures_corners = np.int0(goodfeatures_corners) #ȥ����ֵ���С���㣬��Ϊ��������������������
print(len(goodfeatures_corners))
# ע��ѧϰ���ֱ����ķ�����д����
for i in goodfeatures_corners:
    
    #ע�⵽i �����б�ΪԪ�ص��б�������Ҫflatten����ravelһ�¡�    
    x,y = i.flatten()
 
    cv2.circle(img,(x,y), 5, [0,255,], -1)
     
cv2.imshow('goodfeature',img)
 
cv2.waitKey()
