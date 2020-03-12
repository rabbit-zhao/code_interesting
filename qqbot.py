# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2019-12-13 01:02:49
# @Last Modified by:   zhr
# @Last Modified time: 2019-12-13 01:05:12
from qqbot import _bot as bot

bot.Login(['-q', '1030635594'])

buddy = bot.List('buddy', '洛安。')

if buddy:
	b = buddy[0]
	bot.SendTo(b, '00')