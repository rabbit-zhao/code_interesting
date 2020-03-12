# -*- coding: utf-8 -*-
# @Author: zhr
# @Date:   2020-03-02 16:41:43
# @Last Modified by:   zhr
# @Last Modified time: 2020-03-11 15:30:18

# chpfsfqevbfbbfee
from email.mime.text import MIMEText
import smtplib
import datetime
import schedule
import time

def send():
	that_day = datetime.datetime(2020, 12, 19)
	days = (that_day - datetime.datetime.now()).days

	# 文本
	msg = MIMEText('考研倒计时%d天' % days)
	# 主题
	msg['Subject'] = '考研倒计时%d天' % days

	sender = '1030635594@qq.com'
	# 授权码
	password = "授权码"
	host = "smtp.qq.com"
	receiver = "1030635594@qq.com"

	try:
		# QQ邮箱端口号为465
		server = smtplib.SMTP_SSL(host, 465)
		# 登录 发送 退出
		server.login(sender, password)
		server.sendmail(sender, [receiver], msg.as_string())
		server.quit()
		print("success")
	except:
		print("failed")

schedule.every().day.at("09:23").do(send)

while True:
	schedule.run_pending()
	time.sleep(10)
