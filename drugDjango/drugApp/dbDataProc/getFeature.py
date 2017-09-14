# -*- coding: utf-8 -*-
#get  feature from  data to form  drugFeature
from drugApp.drugClass.DrugStruc import dFeature
import jieba
import jieba.analyse
import re

class drugFeaturer(object):
	"""docstring for drugFeaturer"""
	def __init__(self):
		pass
		

	def getFeature(self,drugList):
		features=[]
		featurers=[]

		for each in drugList:
			keyWordList=each.drugFeatureKeyWords.split(",")
			#for each
			if each.featureName not in features:
				drugs=[each.drugname]
				strSubFeatures=each.drugFeatureContent
				subfeatures={}
				#print strSubFeatures
				for ekey in keyWordList:
					subfeatures[ekey]=1
				#subfeatures[each.drugFeatureKeyWords]=1
				newFeature=dFeature(each.featureName, 1, drugs, subfeatures)
				featurers.append(newFeature)
				features.append(each.featureName)
			else:
				for drugfeature in featurers:
					if each.featureName==drugfeature.feature:
						#keyWordList=each.drugFeatureKeyWords.split(",")
						for fdrug in  keyWordList:
							
							# print drugfeature.subfeatures.keys()
							if fdrug  in drugfeature.subfeatures.keys():
								# print "ok"
								# #print 
								# print drugfeature.subfeatures[fdrug]
								drugfeature.subfeatures[fdrug]=drugfeature.subfeatures[fdrug]+1
								#print drugfeature.subfeatures[fdrug]
							else:
								drugfeature.subfeatures[fdrug]=1
								#subfeatures[each.drugFeatureKeyWords]=subfeatures[each.drugFeatureKeyWords]+1
								#drugfeature.subfeatures=drugfeature.subfeatures+","+fdrug
						#drugfeature.subfeatures=drugfeature.subfeatures+each.drugFeatureKeyWords
						drugfeature.featureNum+=1
						drugfeature.drugs.append(each.drugname)
						break

		
		reFeature=[]
		for each in featurers:
			seconfeature=[]
			if each.featureNum>1:
			        	for esubfeature in each.subfeatures.keys():
			        		# print esubfeature
			        		
			        		if each.subfeatures[esubfeature]>1:
			        			seconfeature.append(esubfeature)
			        	# print "****"
			        	each.subfeatures=seconfeature
			        	for x in each.subfeatures:
			        		print x

			        	reFeature.append(each)
		return reFeature

	#get second feature 
	def  getSubFeatures():
		pass

	#get Feature Class
def  getFeatureClasses(drugFeature,topK):
	#print drugFeature
	rs=re.split(r'["0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"]', drugFeature)
	drugText="".join(rs)
	# print "drugRe+++++++"
	# print drugText
	#print drugText
	tags = jieba.analyse.extract_tags(drugText, topK=topK)
	# rlist=[]
	# for each in tags:
	# 	peach=each.replace(".","")
	# 	percent=peach.replace("%", "")
	# 	num=percent.isdigit()
		
	# 	if  not num:
	# 		rlist.append(num)
	#print(",".join(rlist))
	# print "tag"
	# print ",".join(tags)
	return(",".join(tags))



# drugFeature="化学名称：4-(4-3-[4-氯-3-(三氟甲基)苯基]脲基苯氧基)-N2-甲基吡啶-2-羧酰胺-4-甲苯磺酸盐\n分子式：C21H16CIF3N4O3·C7H8O3S\n分子量：637.0"
# drugFeature="123化学名称：4脲基苯氧"
# getFeatureClasses(drugFeature, 10)		