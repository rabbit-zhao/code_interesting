# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2019-10-25 20:26:04
# @Last Modified by:   zhr
# @Last Modified time: 2019-10-30 10:51:18
from opencc import OpenCC
from zhon.hanzi import punctuation
import os
import re

f = open("laoliangjia.txt", "r", encoding="utf-8")
text = f.readlines()
text = str(text[0])   # 转化为字符串，注意text为只有一个元素的列表
text = re.sub(r"[%s]+" %punctuation, "", text)   # 去标点
print(text[:100], "\n")

cc = OpenCC("t2s")
text2 = cc.convert(text)   # 转简体

text_list = list(text)
text2_list = list(text2)   # 字符串变列表
n = 0
for w in text_list:        # 找两列表不一样，即繁体字数量
	if w not in text2_list:
		n += 1
print(n, "\n")     

print(len(text_list), " ", len(text2_list))   # 字数

num = 0  # 同字个数
for i in range(len(text2_list)):   
	if text2_list[i] in text2_list[i+1:]:   # 如果该字在其后面的列表中出现
		print(text2_list[i], text2_list[i-(i%4):i-(i%4)+4])  # 输出四字
		index2 = text2_list.index(text2_list[i], i+1)   # 索引
		print(text2_list[index2], text2_list[index2-(index2%4):index2-(index2%4)+4])   # 重复的字所在四字
		num += 1
print(num)
