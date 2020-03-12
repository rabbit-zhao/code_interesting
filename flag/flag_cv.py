import cv2
from PIL import Image
from PIL import ImageTk

def deal_flag(pic_path):
	# pic_path.replace("/", "")
	img_head = cv2.imread(pic_path)
	img_flag = cv2.imread("flag.jpg")
	w_head, h_head = img_head.shape[:2]
	w_flag, h_flag = img_flag.shape[:2]

	scale = w_head / w_flag / 4
	img_flag = cv2.resize(img_flag, (0,0), fx = scale, fy = scale)

	w_flag, h_flag = img_flag.shape[:2]
	for c in range(0,3):
		img_head[w_head-w_flag:, h_head-h_flag:, c] = img_flag[:, :, c]
	cv2.imwrite("new.jpg", img_head)

	img = cv2.cvtColor(img_head, cv2.COLOR_BGR2RGB)
	img = Image.fromarray(img)
	img = ImageTk.PhotoImage(img)

	return img 
cv2.

d = "C:/Users/zhr/Desktop/color.png"
deal_flag(d)
