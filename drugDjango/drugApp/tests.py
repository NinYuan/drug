# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


import jieba
import jieba.analyse
# a=[u'\u614e\u7528', u'\u8f7b\u81f3', u'\u4e2d\u5ea6', u'\u836f\u7269', u'\u672c\u54c1', u'\u7814\u7a76', u'\u8f93\u6db2', u'\u9759\u8109\u6ce8\u5c04', u'\u4f7f\u7528', u'\u53d1\u751f', u'\u5987\u6027', u'\u53cd\u5e94', u'\u7ec4\u80fa', u'\u60a3\u8005', u'\u7981\u7528', u'\u7528\u836f']
# for e in a:
# 	print e
# print u'\u4e25\u91cd'
# a=[1,2,3]
# a={"a":1,"b":2}
# b=[1,4,5]
# for  e in b:
# 	if e in a.keys():
# 		print "yes"

# for b in a.keys():
# 	print b
# a="13.4%"
# import re
# ss="123健康人单次皮下注射胸腺法新1.6mg，血药峰浓度约为37.51ng/ml，达峰时间约为1.67小时，AUC0-15约为152.15ng/ml·h，半衰期约为1.65小时。"
# rs=re.split(r'["0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"]', ss)
# rs.remove("")

# print "".join(rs)

# 		peach=each.replace(".","")
# 		percent=peach.replace("%", "")
# 		num=percent.isdigit()

# def  getFeatureClasses(drugFeature,topK):
# 	tags = jieba.analyse.extract_tags(drugFeature, topK=topK)
# 	rlist=[]
# 	for each in tags:
# 		a="13.4%"
# 		peach=each.replace(".","")
# 		percent=peach.replace("%", "")
# 		num=percent.isdigit()
# 		print each
# 		if  not num:
# 			rlist.append(each)
# 	print(",".join(rlist))
# 	pass


# # drugFeature="化学名称：4-(4-3-[4-氯-3-(三氟甲基)苯基]脲基苯氧基)-N2-甲基吡啶-2-羧酰胺-4-甲苯磺酸盐\n分子式：C21H16CIF3N4O3·C7H8O3S\n分子量：637.0"
# drugFeature="123化学名称：4脲基苯氧"
# getFeatureClasses(drugFeature, 10)	

# a="13.4%"
# c=a.replace(".","")
# e=c.replace("%", "")
# b=e.isdigit()
# print b

# def  getFeatureClasses(drugFeature,topK):
# 	tags = jieba.analyse.extract_tags(drugFeature, topK=topK)
# 	print(",".join(tags))
# 	return ",".join(tags)
# def  ok():
	
# 	drugFeature="化学名称：4-(4-3-[4-氯-3-(三氟甲基)苯基]脲基苯氧基)-N2-甲基吡啶-2-羧酰胺-4-甲苯磺酸盐\n分子式：C21H16CIF3N4O3·C7H8O3S\n分子量：637.0"
# 	drugFeature="本品主要成份及其化学名称为:(Z)-N-[2-(二乙胺基)乙基-5-[(5-氟-2-氧代-1,2-二氢-3H-吲哚-3-亚基)甲基]-2,4-二甲基-3-氨甲酰-1H-吡咯苹果酸盐其结构式为:分子式：C22H27FN4O2 ·C4H6O5　　分子量：532.6　　辅料名称：甘露醇、交联羧甲基纤维素钠、聚维酮（K-25）和硬脂酸镁"
# 	drugFeature="是一种新型多靶向性的治疗肿瘤的口服药物，用于治疗无法手术或远处转移的肝细胞癌。"
# 	drugFeature="索拉非尼是多种激酶抑制剂体外试验显示它可抑制肿瘤细胞增殖和抗血管生成作用。索拉非尼抑制肿瘤细胞的靶部位CRAF、BRAF、V600EBRAF、c-Kit、FLT-3和肿瘤血管靶部位的CRAF、VEGFR-2、VEGFR-3、PDGFR-β。RAF激酶是丝氨酸/苏氨酸激酶，而c-Kit、FLT-3、VEGFR-2、VEGFR-3、PDGFR-β为络氨酸激酶，这些激酶作用于肿瘤细胞信号通路、血管生成和凋亡。 体内试验显示，在多种人肿瘤抑制裸鼠模型中，如人肝细胞肿瘤、肾细胞肿瘤中，可抑制肿瘤生长和血管生成。"
# 	df=drugFeature.split("。")
# 	featureContentlist=[]
# 	for each in df:
# 		featureContent=getFeatureClasses(each, 3)
# 		featurelist=featureContent.split(",")
# 		featureContentlist=featureContentlist+featurelist
# 	print ",".join(featureContentlist)
# #cutText(drugFeature)
# #ok()
# print "****"
# drugFeature="索拉非尼是多种激酶抑制剂体外试验显示它可抑制肿瘤细胞增殖和抗血管生成作用。索拉非尼抑制肿瘤细胞的靶部位CRAF、BRAF、V600EBRAF、c-Kit、FLT-3和肿瘤血管靶部位的CRAF、VEGFR-2、VEGFR-3、PDGFR-β。RAF激酶是丝氨酸/苏氨酸激酶，而c-Kit、FLT-3、VEGFR-2、VEGFR-3、PDGFR-β为络氨酸激酶，这些激酶作用于肿瘤细胞信号通路、血管生成和凋亡。 体内试验显示，在多种人肿瘤抑制裸鼠模型中，如人肝细胞肿瘤、肾细胞肿瘤中，可抑制肿瘤生长和血管生成。"

# featureContent=getFeatureClasses(drugFeature, 10)
# print featureContent
# def  cutText(drugFeature):

# 	seg_list = jieba.cut(drugFeature)  # 默认是精确模式
# 	print(", ".join(seg_list))
# 	return