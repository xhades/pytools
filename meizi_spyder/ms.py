#!usr/bin/env python
#-*-coding:utf-8 -*-
# author:xhades
#version 1.0
#date:1/8/2016

import urllib,urllib2
import re,os
from time import sleep

class spider(object):
	def __init__(self):
		self.lst_girl = []
		self.lst_fail = []
		self.lst_use = []
		self.lst_PATH = os.getcwd()
		self.host = 'http://www.zngirls.com/'

	# def saveImg(self,fdir,img_url):
	# 	fn = img_url.split('/')

	#保存图片到硬盘
	def save_imgs(self,fdir,img_url):
		fn = img_url.split('/')
		try:
			data = urllib2.urlopen(img_url,timeout=20).read()
			f = open(fdir+'\\'+fn[-1],'wb')
			f.write(data)
			f.close()

			print 'save image =======ok'

		except:
			print  'save image error ====ok'

			f = open('fdir'+'\\err.txt','w' )
			f.write(img_url)
			f.close()
	# 如果不存在 我们就创建他
	def mkdir(self,fdir):
		ie = os.path.exists(fdir)
		if not ie:
			os.makedirs(fdir)

	# 获取所有的妹子
	def getGirllist(slef):
		url = 'http://www.zngirls.com/ajax/girl_query_total.ashx'
		# 浏览器头信息
		header = {
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
				'Host':'www.zngirls.com',
				'Origin':'http://www.zngirls.com',
				'Referer':'http://www.zngirls.com/find/',
				'X-Requested-With':'XMLHttpRequest'
		}

		i = 1
		go = True
		girlUrls = []
		while go:
			postdata = {
					'country':'韩国',
					'curpage':str(i),  #为什么是str(i)
					'pagesize':'20'
			}
			post_data = urllib.urlencode(postdata)
			req = urllib2.Request(url,post_data,header)
			html = urllib2.urlopen(req).read()
			#print html
			pat = re.compile('/girl/[\d]+')
			girl_url = re.findall(pat,html)
			girlUrls += girl_url
			print'初始化完成页数：'+str(i)
			if len(girl_url)>1:
				go = True
				i+=1
			else:
				go = False
			#print girlUrls

			girllists = list(set(girlUrls))
			fp = open('girls.txt','w')
			for s in girllists:
				fp.write(s+'\n')
			fp.close()
			print '初始化完成===================ok'
			print '获取数据的长度：'+str(len(girllists))
			return girllists

	



if __name__ == '__main__':
	girl = spider()
	girl.getGirllist()





