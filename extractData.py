# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from getData.getDrugsInt import *


class  extractDrugs(object):
	"""docstring for  extractDrugs"""
	def __init__(self, html,tag,dictionlist):
		
		self.html= html
		self.tag=tag
		self.dictionlist=dictionlist
		

	def   getDrug(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		
		sections=soup.find_all(self.tag)     
		texts=[]
		for section in sections:
			text=section.strings
			for etext in text:
				texts.append(etext)

		   

		
		drugDic={}
		for i in range(len(texts)):
			
			boolExtract=False
			boolExtract=self.__extractInfo(texts[i])

			
			
			if  boolExtract:
				if  texts[i] not in drugDic.keys():

					drugDic[texts[i]]=texts[i+1]
					#print texts[i]
					#print texts[i+1]
				i=i+2
			else:
				i=i+1
		return drugDic
				

	def    __extractInfo(self,text):
		
		for point in self.dictionlist:
			
			if  text.startswith(point):
			
				return True
		return False








	
