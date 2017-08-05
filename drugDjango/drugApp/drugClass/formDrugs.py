# -*- coding: utf-8 -*-
from drugApp.drugClass.DrugStruc import *
import sys
import string
#from DrugStruc import *
class  drugFormer(object):
	"""docstring for  drugFormer"""
	def __init__(self, drugDict,drugInterLabel,drugByNameLabelList,removeDict):
		
		self.drugDict = drugDict
		self.drugInterLabel=drugInterLabel
		self.drugByNameLabelList=drugByNameLabelList
		self.removeDict=removeDict

	def   formDrug(self):
		drugList=[]
		for  drugClass in self.drugDict.keys():
			drugNames=self.drugDict[drugClass]
			drugs=self.__getDrugName(drugClass, drugNames)
			drugList=drugList+drugs
			
		return drugList

	def  __getDrugName(self,drugClass,drugNames):
		reload(sys)
		
		sys.setdefaultencoding("utf8")
		reDrugs=[]
		drugList=drugNames.split(self.drugInterLabel)
		for edrug in drugList:
			drugNamelist=edrug.split(self.drugByNameLabelList[0])
			
			drugname=drugNamelist[0]
			if len(drugNamelist)==1:
				drugNamelist=edrug.split(self.drugByNameLabelList[1])
			if len(drugNamelist)==1:
				eachDrug=drug(drugname, "None", drugClass)
				reDrugs.append(eachDrug)
				continue
			drugByName=drugNamelist[1]

			drugByName=self.__removeDict(drugByName, self.drugByNameLabelList)

			drugClass=self.__removeDict(drugClass,self.removeDict)
			drugname=self.__reSamstr(drugname, drugByName)
			eachDrug=drug(drugname, drugByName, drugClass)
			reDrugs.append(eachDrug)
		return reDrugs
			
	def  __removeDict(self,stringdm,lablelist):
		
		
		for elable in lablelist:
			
			try:
				#stringdm=stringdm.replace(elable,"")
				stringdm=string.replace(stringdm,elable,"")
			except Exception as e:
				pass

		
		return stringdm
		
	def  __reSamstr(self,MainString,substring):
		k=MainString.find(substring)
		
		if k==-1:
			return MainString
		MainString=MainString[:k-1]
		return MainString
		

# drugDict={"sd":"sdf(1),ge(124)","wefr":"hi(11),iu(888)"}
# drugInterLabel=","
# drugByNameLabelList=["(",")"]
# drugFm=drugFormer(drugDict, drugInterLabel, drugByNameLabelList)
# drugList=drugFm.formDrug()
# for each in drugList:
# 	print each.drugname,each.drugByname,each.drugClass
