# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2020-02-19 21:15:26
# @Last Modified by:   zhr
# @Last Modified time: 2020-02-25 21:15:17
import cv2 as cv
import numpy as np 
from PIL import ImageFont, ImageDraw, Image

# 导入瓶子并滤波
bottle = cv.imread("bottle.jpg")
bottle2 = cv.fastNlMeansDenoisingColored(bottle)

# 输入参数
row = int(input("行："))
col = int(input("列："))
title = input("题目：")
print("输入文字： ")
writ = []
for i in range(row*col):
	zi = input("{}：".format(i+1))
	writ.append(zi)

# 瓶子左右间距、上下间距
span_w = 0.4
span_h = 0.8


(bottle_h, bottle_w, _) = bottle2.shape

background2 = np.ones((int((row+row*span_h-span_h+2)*bottle_h), int(((col+1)*span_w+col)*bottle_w), 3), dtype="uint8")*250

# 起始点
stx = span_w * bottle_w
sty = bottle_h

# 画瓶子
for c in range(col):
	for r in range(row):
		stx2 = int(stx + (1+span_w)*bottle_w*c)
		sty2 = int(sty + (1+span_h)*bottle_h*r)
		print(stx2, sty2)
		for i in range(0, bottle_h-1):
			for j in range(0, bottle_w-1):
				background2[sty2+i, stx2+j] = bottle2[i, j]

# 写字
fontpath = "zi.ttf"
font = ImageFont.truetype(fontpath, 20)
img_pil = Image.fromarray(background2)
draw = ImageDraw.Draw(img_pil)

num = 0
for c in range(col):
	for r in range(row):
		stx2 = int(stx + (1+span_w)*bottle_w*c)
		sty2 = int(sty + (1+span_h)*bottle_h*r)
		# background2 = cv.putText(background2, writ[num], (stx2+int(0.1*bottle_w), sty2+int(1.3*bottle_h)), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,0,0), 2)
		draw.text((stx2+int(0.2*bottle_w), sty2+int(1.2*bottle_h)),  writ[num], font = font, fill = (0,0,0))
		num += 1

font = ImageFont.truetype(fontpath, 30)
draw.text((int(0.4*background2.shape[1]), int(0.5*bottle_h)),  title, font = font, fill = (0,0,0))

bk_img = np.array(img_pil)
 
cv.imshow("add_text",bk_img)
cv.waitKey(0)