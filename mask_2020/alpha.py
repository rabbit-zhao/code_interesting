# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2020-01-22 20:09:07
# @Last Modified by:   zhr
# @Last Modified time: 2020-01-22 20:37:28
import numpy as np
import cv2

img = cv2.imread("portrait.jpg")
co = cv2.imread("mask2.png", -1)
scr_channels = cv2.split(co)
dstt_channels = cv2.split(img)
b, g, r, a = cv2.split(co)
for i in range(3):
	dstt_channels[i][100:200,300:400] = dstt_channels[i][100:200,300:400]*(255.0-a)/255
	dstt_channels[i][100:200,300:400] += np.array(scr_channels[i]*(a/255), dtype=np.uint8)
cv2.imwrite("img_target.png", cv2.merge(dstt_channels))
