# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2020-01-22 15:28:26
# @Last Modified by:   zhr
# @Last Modified time: 2020-02-25 21:15:17
import cv2
import numpy as np 
import dlib

def key_points(img):
	points_key = []
	PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(PREDICTOR_PATH)
	rects = detector(img, 1)

	for i in range(len(rects)):
		landmarks = np.matrix([[p.x, p.y] for p in predictor(img, rects[i]).parts()])
		print(landmarks)
		for idx, point in enumerate(landmarks):    # 特定点，可直接提取
			print(idx)
			pos = (point[0, 0], point[0, 1])
			print(pos)
			if idx in [2, 8, 14, 28]:
				points_key.append(pos)
				# cv2.circle(img, pos, 2, (255, 0, 0))

	return(points_key)

def wear_mask(mask_img, face_img):
	h_mask, w_mask = mask_img.shape[:2]   # 高，宽
	gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
	face_keys = key_points(gray)
	left = face_keys[0][0]
	jaw = face_keys[1][1]
	right = face_keys[2][0]
	nose = face_keys[3][1]
	w_mouth = right - left
	h_mouth = jaw - nose
	mask_img = cv2.resize(mask_img, (w_mouth, h_mouth))
	
	mask_channels = cv2.split(mask_img)
	face_channels = cv2.split(face_img)
	b, g, r, a = cv2.split(mask_img)
	ans_img = face_img.copy()
	print(nose, nose+h_mouth, left, left+w_mouth)
	for c in range(0, 3):
		face_channels[c] = np.array(face_channels[c], dtype=np.uint8)
		k = np.uint8((255.0-a)/255.0)
		face_channels[c][nose:nose+h_mouth, left:left+w_mouth] = face_channels[c][nose:nose+h_mouth, left:left+w_mouth]*k
		mask_channels[c] *= np.array(a/255, dtype=np.uint8)
		face_channels[c][nose:nose+h_mouth, left:left+w_mouth] += np.array(mask_channels[c], dtype=np.uint8)
	ans = cv2.merge(face_channels)

	return ans

face_img = cv2.imread("try10.jpg")
mask_img = cv2.imread("ma.png", -1)
ans_img = wear_mask(mask_img, face_img)

cv2.imwrite("ans10.jpg", ans_img)
cv2.imshow("ans", ans_img)
cv2.waitKey(0)
