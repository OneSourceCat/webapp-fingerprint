#coding=utf-8
import requests
import json
import urllib
import sys
import os
import socket
import time
import re
from bs4 import BeautifulSoup
from dede_feature import matches
from util import Util
from dede_recommend_exploit import DedeAttacker
from ip_reverse import IPReverse
from scanner import Scanner
'''
检测DEDEcms
1.robots.txt
2.检测网页Powered by 字样
Usge：
Args：域名列表
return：dedecms  webapp列表
'''
class DetectDeDeCMS():
	#检测robots.txt
	def detectingRobots(self,url):
		robots_content = matches['robots']
		robots_url = "%s/%s" % (url,'robots.txt')
		robots_page = requests.get(robots_url)
		if robots_page.status_code != 200:
			return False
		content = robots_page.content
		#检索robots与插件中的是否一致
		for x in robots_content:
			if content.count(x) != 0:
				return True
			else:
				return False

	#powered by dede 检测
	def detectingPoweredBy(self,raw_page):
		soup = BeautifulSoup(raw_page)
		dede_intext = matches['intext']
		for x in dede_intext:
			pattern = re.compile(x)
			try:
				text = soup.a.text
			except Exception, e:
				return False
			if pattern.findall(text) != []:
				return True
			else:
				return False

	def getResult(self,url):
		url = 'http://%s' % url
		try:
			r = requests.get(url)
			raw_page = r.content
		except Exception, e:
			return False
		if (not r) or (r.status_code != 200) or (not raw_page):
			return False
		is_robots_exists = self.detectingRobots(url)
		is_poweredby_exists = self.detectingPoweredBy(raw_page)
		if is_poweredby_exists or is_robots_exists:
			return True
		else:
			return False