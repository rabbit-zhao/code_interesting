# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2020-03-05 08:54:47
# @Last Modified by:   zhr
# @Last Modified time: 2020-03-05 12:32:49
import jieba
import re
import collections
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np 

f1 = open("滚去学习(2377919782).txt", "r", encoding="utf-8")
zhr_name = ["东都大白兔", "name=main", "今天必须早睡"]
zyf_name = ["18 环境 张一帆", "洛安。", "帆大讯飞", "小帆讯飞", "别找她！舔狗！", "别生气，别冲动，别理她", "快去学习", "滚去学习"]
timepat = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")

nzyf = 0
nzhr = 0
flag = 0
lines = f1.readlines()
zyf_s = []
zhr_s = []
for line in lines:
	line = line.replace("[图片]", "")
	line = line.replace("[表情]", "")
	line = line.replace("\n", "")
	if flag == "zyf":
		zyf_s.append(line)
		flag = 0
	if flag == "zhr":
		zhr_s.append(line)
		flag = 0
	if re.search(timepat, line):
		for w in zyf_name:
			if w in line:
				flag = "zyf"
				break
		for w in zhr_name:
			if w in line:
				flag = "zhr"
				break

print(len(zhr_s))
print(len(zyf_s))
print(zhr_s[0:20])

remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要',u'我',u'你',u'？',u"",u" ",u"就",u"不","啊",
                u"吧",u"也",u"不是",u"就是",u"什么",u"怎么",u"这个",u"这么",u"一个"]
k = 0
words = []
for s in zyf_s:
	if "赵先生" in s:
		words.append("赵先生")
	k += 1
	thelist = jieba.cut(s, cut_all = False)
	for word in thelist:
		if word not in remove_words:
			if len(word) > 1:
				words.append(word)
			if k < 20:
				print(word)

word_counts = collections.Counter(words)
words_top10 = word_counts.most_common(50)
print(words_top10)

mask = np.array(Image.open("cloud2.jpeg"))
wc = wordcloud.WordCloud(
	background_color="black",
	font_path='zi.ttf',
	mask=mask,
	max_words=200,
	max_font_size=500
	)

wc.generate_from_frequencies(word_counts)
image_colors = wordcloud.ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.savefig("zyf2.png", dpi=1000)
plt.show()









