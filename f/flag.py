import tkinter.filedialog
# import tkinter as tk 
from tkinter import Button, Tk, Label
import os 
# import flag_cv as fc 
from PIL import Image
from PIL import ImageTk
from cv2 import imread, imwrite, cvtColor, resize, COLOR_BGR2RGB

def resource_path(relative_path):    
    base_path = getattr(        
        sys, '_MEIPASS', os.path.dirname(            
            os.path.abspath(__file__)))    
    return os.path.join(base_path, relative_path)
    
# global_popu_Dic = resource_path("res/flag.jpg") 
global_popu_Dic = "res/flag.jpg"

def deal_flag():
	global panelA, panelB
	global file_path
	global img_save

	file_path = tkinter.filedialog.askopenfilename(title="选择图像", \
		filetypes = [("PNG",".png"), ("JPG", ".jpg")])
	if file_path is not None :
		img_head = imread(file_path)
		img_head1 = img_head.copy()
		img_flag = imread(global_popu_Dic)
		# imwrite("D:/f.jpg", img_flag)
		w_head, h_head = img_head.shape[:2]
		w_flag, h_flag = img_flag.shape[:2]

		scale = w_head / w_flag / 4
		img_flag = resize(img_flag, (0,0), fx = scale, fy = scale)

		w_flag, h_flag = img_flag.shape[:2]
		for c in range(0,3):
			img_head[w_head-w_flag:, h_head-h_flag:, c] = img_flag[:, :, c]

		img_save = img_head.copy()

		img_head = cvtColor(img_head, COLOR_BGR2RGB)
		img_head1 = cvtColor(img_head1, COLOR_BGR2RGB)

		img_head = Image.fromarray(img_head)
		img_head1 = Image.fromarray(img_head1)

		img_head = ImageTk.PhotoImage(img_head)
		img_head1 = ImageTk.PhotoImage(img_head1)

	# if panelA is None or panelB is None:
	if file_path is not None:
		panelA = Label(image = img_head1)
		panelA.image = img_head1
		panelA.pack(side="left", )

		panelB = Label(image = img_head)
		panelB.image = img_head
		panelB.pack(side="right")

def save_file():
	global file_path
 	# img_save
	file_path = tkinter.filedialog.asksaveasfilename(title="保存图片", filetypes = [("PNG",".png")])
	if file_path is not None:
		# print(file_path)
		imwrite(file_path+".png", img_save)


window = Tk(screenName="国旗+头像")
panelA = None
panelB = None

btn2 = Button(window, text="保存图像", command = save_file)
btn2.pack(side="bottom")

btn1 = Button(window, text="选择图像", command = deal_flag)
btn1.pack(side="bottom")

l = Label(text="QQ:1030635594")
l.pack()

window.mainloop()