# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from drugApp.getData.getDrugsInt import *
import re

# class spider(object):
# 	"""docstring for spider"""
# 	def __init__(self,url):
# 		self.url = url
# 	def  getData(self):
# 		f=urllib.urlopen(self.url)
# 		html= f.read()
# 		return html

class  extractDrugs(object):
	"""docstring for  extractDrugs"""
	#def __init__(self, html,tag,rpattern):
	def __init__(self, html,tag):
		
		self.html= html
		self.tag=tag
		# self.rpattern=rpattern
		

	def   getDrug(self,rpattern):
		soup = BeautifulSoup(self.html, 'html.parser')
		
		sections=soup.find_all(self.tag) 
		
		texts=[]
		for section in sections:
			
			text=section.strings
			for etext in text:
				
				texts.append(etext)
		# print "text"
		# for etext in texts:
		# 	print repr(etext)


		

		if len(rpattern)==0:
			# print "*********"
			return texts
		rtext=[]
		print "text"
		for etext in texts:
			#print etext
			# if etext.find('\n')!=-1:
			# 	continue
			rtext=rtext+self.extractDrug(etext,rpattern)

		return rtext

	def extractDrug(self,etext,rpattern):
		# print "etext"
		# print etext
		# print self.rpattern
		# print repr(rpattern)
		

		s=re.split(rpattern,etext)
		# print "s"
		# print s
		if len(s)>2:
			return s
		else:
			return []
		# if len(s)==1:
		# 	return []

		# for etext in s:
			
		# 	if len(etext)>18:
		# 		print "lent"
		# 		print len(etext)
		# 		print "****************"
		# 		s.remove(etext)
		# # print "s"
		# print s
		# for each in s:
		# 	print each
		
		# s=re.split(self.rpattern,"".join(s))
		# s=re.split(self.rpattern,"".join(s))
		#print s
		# return s
		

# file="/home/hong/桌面/大四医疗信息系统设计/[菩提众生]抗肿瘤药大全.html"
# html=open(file).read()
# tag="p"
# rpattern='[（|、|）|其中|的]'
# exdata=extractDrugs(html, tag)
# drugNameText=exdata.getDrug(rpattern)
# for each in drugNameText:
# 	print each


# url="http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ"
# sp=spider(url)
# html=sp.getData()


# dictionlist=[ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

# tag="section"
# exdata=extractDrugs(html, tag, dictionlist)
# drugDict=exdata.getDrug()


# for each in drugDict.keys():
# 	print each
# 	print drugDict[each]






	
