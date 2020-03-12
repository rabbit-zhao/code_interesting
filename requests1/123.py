import urllib.request
import re
import requests
import requests
from bs4 import BeautifulSoup
from lxml import html
import os
import time
from selenium import webdriver#导入库
# drive_path = r"E:/anaconda3/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
# browser = webdriver.Firefox()#声明浏览器
# url = 'https:www.baidu.com'
# browser.get(url)#打开浏览器预设网址
# print(browser.page_source)#打印网页源代码
# browser.close()#关闭浏览器
etree=html.etree
turl = "https://www.2717.com/tag/1771.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/73.0.3683.86 Safari/537.36',
    #'Referer': "http://so.news.cn/?keyWordAll=%E4%BF%9D%E9%99%A9&keyWordOne=&keyWordIg=&searchFields=0&sortField=0&url=&senSearch=1&lang=cn#search/0/%E4%BF%9D%E9%99%A9/"
}

# req=urllib.request.Request(url=turl,headers=aaa)
# a=urllib.request.urlopen(req).read()
r=requests.get(turl, headers=headers).content
soup = etree.HTML(r)

# soup = etree.tostring(soup)
print(soup)
# page_url = soup.xpath("//div[@class='show_nav_bar']/a/@href")
page_url = soup.xpath("//ul[@id='Tag_list']//a[@target='_blank']/@href")
print(page_url)

r2 = requests.get("https://www.2717.com"+page_url[0], headers=headers).content
soup2 = etree.HTML(r2)
print(soup2)
pic_url = soup2.xpath("//p[@align='center']//img/@src")
aa = soup2.xpath("//h1/text()")
bb = soup2.xpath("//li[@class='thisclass']//a[@id='viewPic']//@target")
print(aa)
print(pic_url)
print(bb)
image_data = requests.get(pic_url[0], headers=headers)
file_name = "1.jpg"
with open(file_name, "wb") as f:
	f.write(image_data.content)
	f.close()