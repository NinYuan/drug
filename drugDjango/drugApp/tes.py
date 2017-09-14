# -*- coding: utf-8 -*-
from drugApp.models import drugFeature
from drugApp.tests import *
from drugApp.dbDataProc.getFeature import getFeatureClasses
import jieba
import jieba.analyse

# def  getFeatureClasses(drugFeature,topK):
# 	tags = jieba.analyse.extract_tags(drugFeature, topK=topK)
# 	print(",".join(tags))
# 	return ",".join(tags)
def chance(request):
    drugList = drugFeature.objects.all()
    i=0
    for each in drugList:

    	featureContent=getFeatureClasses(each.drugFeatureContent, 15)
    	print "drugFeatureKeyword"
    	print each.drugFeatureKeyWords
    	test1 = drugFeature.objects.get(drugname=each.drugname,featureName=each.featureName,drugFeatureContent=each.drugFeatureContent)
    	test1.drugFeatureKeyWords = featureContent
    	test1.save()
    	print "now is "+str(i)
    	print featureContent
    	i=i+1

# chance()  	