# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2019-12-27 18:21:54
# @Last Modified by:   zhr
# @Last Modified time: 2019-12-27 18:34:19
import cv2
import numpy as np 

def CannyThreshold(lowThreshold):
	detected_edges = cv2.GaussianBlur(gray)

original_img = cv2.imread("zyf.jpg")

img1 = cv2.GaussianBlur(original_img, (5, 5), 0)
canny = cv2.Canny(img1, 30, 50)

cv2.imshow("zyf", canny)
cv2.imwrite("zyf1.jpg", canny)
cv2.waitKey(0)
