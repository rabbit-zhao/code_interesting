# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-11-08 23:18:37
# @Last Modified by:   zhr
# @Last Modified time: 2019-11-17 22:18:59
import os
import exifread
import shutil

def exifread_infos(path, photo):
	f = open(path + "/" + photo, "rb")
	tags = exifread.process_file(f)
	EXIF_data = tags["EXIF DateTimeOriginal"].printable
	return(EXIF_data)

# print(os.getcwd())

path = "C:/Users/zhr/Desktop/vivo_2019_11"
dirs = os.listdir(path)
folders = []
n = 0
for file in dirs:
	n += 1
	if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".png"):
		pre_file = file.split(".")[0]
		now_dir = os.path.join(path, file)
		try:
			date = exifread_infos(path, file)
			date_str = date[0:4] + date[5:7] + date[8:10]
			# print(date_str)
			folder = date_str[0:4]
			if folder not in folders:
				folders.append(folder)
				try:
					os.mkdir(os.path.join(path, folder))
				except:
					pass
			new_file = str(n) + "_" + date_str + "." + file.split(".")[1]
			new_dir = path + "/" + folder + "/" + new_file
			print(new_dir)
			shutil.copy(now_dir, new_dir)
		except:
			continue


		

