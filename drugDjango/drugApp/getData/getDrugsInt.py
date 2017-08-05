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
# url="https://baike.baidu.com/item/%E7%94%B2%E7%A3%BA%E9%85%B8%E4%BC%8A%E9%A9%AC%E6%9B%BF%E5%B0%BC"
# sp=spider(url)
# html=sp.getData()
# print html
# 甲磺酸伊马替尼（Gleevec)