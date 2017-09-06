# -*- coding: utf-8 -*-
import urllib

# params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# print params
# f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)

class spider(object):
	"""docstring for spider"""
	def __init__(self,url):
		self.url = url
	def  getData(self):
		f=urllib.urlopen(self.url)
		html= f.read()
		return html


# url="http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ"
# url="http://mp.weixin.com/s/FFj-7dvWPJsUPojktW-qjQ"
# sp=spider(url)
# html=sp.getData()
# print html
# 甲磺酸伊马替尼（Gleevec)