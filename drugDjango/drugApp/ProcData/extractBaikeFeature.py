# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
 
from drugApp.models import drugFeature
# from drugApp.getData.getDrugsInt import *
# from drugApp.Tools.dealData import *

class  extractBaikeFeatureClass(object):
	"""docstring for  extractDrugs"""
	def __init__(self, html,drugname,titleClass,paraClass):
		
		self.html= html
		self.drugname=drugname
		self.titleClass=titleClass
		self.paraClass=paraClass
		#self.className=className
		# self.tag=tag
		# self.dictionlist=dictionlist
		

	def   getBaikeFeature(self):
		response = drugFeature.objects.filter(drugname=self.drugname) 
		#return repr(response)
		#return len(response)
		if  len(response) !=0:
			return "alreadyInMysql"
		#return response
		# return "alreadyInMysql"
		# try:
		# 	response = drugFeature.objects.filter(drugname=self.drugname) 
		# 	return "alreadyInMysql"
		# except Exception as e:
		# 		pass
		soup = BeautifulSoup(self.html, 'html.parser')
		
		Section=soup.find(class_=self.titleClass) 
		
		
		Section=Section.parent

		
		info=""
		while  Section!= None:
			
			
			title=self.isTitle(Section)
			if title:
				info=info+"!@#"+title
				Section=Section.next_sibling
				Section=self.getSibling(Section)
				continue
			
			para=self.isPara(Section)
			if  para:
				info=info+"$%^"+para
			else:
				break
					
			Section=Section.next_sibling
			Section=self.getSibling(Section)
			pass
		#print "info"
		#print info
		druglist=info.split("!@#")
		druglist.remove("")
		for drug in druglist:
			drugInfo=drug.split("$%^")
			FeatureName=drugInfo[0]
			drugInfo.remove(FeatureName)
			if len(drugInfo)==1:
				continue
			drugFeatureText="\n".join(drugInfo)
			

			
			#down to DrugFeature
			

			drugFt=drugFeature(drugname=self.drugname, featureName=FeatureName, drugFeature=drugFeatureText)
			drugFt.save()

		

		return self.drugname
		
		

	def  getSibling(self,TitleSibling):
		while TitleSibling=="\n":
			TitleSibling=TitleSibling.next_sibling
		return TitleSibling
	

	def getStrings(self,sections):
		texts=[]
		for section in sections:
			
			text=section.strings
			for etext in text:

				texts.append(etext)
		return texts
		
		
	def  getTitleString(self,section):
		strings=section.strings
		
		i=0
		for string in strings:
			if i==1:
				return string
				
			i=i+1
			
		pass


	def  getParaString(self,section):
		strings=section.strings
		for string in strings:
			print string
		pass
	#test sibling is title or not
	def isTitle(self,section):
		
		titleSections=section.find(class_=self.titleClass) 
		
		if titleSections!=None:
			
			title=self.getTitleString(titleSections)
			return title
		return False

	def isPara(self,section):
		
		paras=section.strings
		para=""
		for epara in paras:
			if epara.find(u'词条图册')!= -1:
			
				return para
			
			if epara.find(u'参考资料')!= -1:
			
				return False

			if epara.find(u'词条标签：')!= -1:
			
				return False
			para=para+epara
		return para
		

			











	
