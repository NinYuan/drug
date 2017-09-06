# -*- coding: utf-8 -*-

 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from drugApp.ProcData.extractData import *
from drugApp.drugClass.formDrugs import *
from drugApp.drugClass.formElem import *
from drugApp.getData.getDrugsInt import *
from drugApp.ProcData.extractBaikeFeature import *
from drugApp.Tools.dealData import *



#show drugBaikeFeatures

def search_baikeFeature(request):
	
	elemList=formElm()
	
	return render(request, 'searchBaikeFeature.html', {'elemList': elemList})
    #return render_to_response('searchDrug.html')
 
# 接收请求数据
def searchBaikeFeature(request):  
	request.encoding='utf-8'
	

	drugnamelist =  request.GET.getlist('drugname')
	baikeFeature=[]

	#return HttpResponse(drugnamelist[0])
	
	#drugname=toUrlCode(drugnamelist[0])
	# drugname=drugnamelist[1].encode("UTF-8") 
	
	# url=url+drugname
	# sp=spider(url)
	# html=sp.getData()
	#className="title-text"

	druglist=[]
	for i in range(len(drugnamelist)):
		drugname=drugnamelist[i].encode("UTF-8") 
		#drugname=toUrlCode(drugnamelist[0])
		#drugname=toUrlCode(drugnamelist[i])
		url="https://baike.baidu.com/item/"
		url=url+drugname
		sp=spider(url)
		html=sp.getData()

		# file="/home/hong/桌面/大四医疗信息系统设计/依维莫司_百度百科.html"
		# html=open(file).read()
		#drugname="依维莫司"
		#titleClass="para-title"
		titleClass="title-text"
		paraClass="para"
		
		
		try:
			exdata=extractBaikeFeatureClass(html,drugname,titleClass,paraClass)

			drugDownedName=exdata.getBaikeFeature()
			druglist.append(drugDownedName)
		except Exception as e:
			pass
	# context={}
 #    	context['para']=druglist
    	return  render(request, 'mysqlResult.html',{'druglist':druglist})


		#return HttpResponse("ok")
		#return HttpResponse(drugDownedName)

	# message=""
		#try:

		# exdata=extractBaikeFeatureClass(html,drugname,className)

		# datalist=exdata.getBaikeFeature()

		# if datalist==False:
		# 	continue
		# for edata in datalist:
		# 	if edata not in baikeFeature:
		# 		baikeFeature.append("*")
		# 		baikeFeature.append(edata)
		# baikeFeature.append("next")

			#baikeFeature=baikeFeature+
		
		# if i==2:
		# 	break
		

	


	# drugFm=drugFormer(drugDict, drugInterLabel, drugByNameLabelList,removeDict)
	# drugList=drugFm.formDrug()

	# message=""
	# for each in drugList:
	# 	message+=each.drugname+"		"+each.drugByname+"		"+each.drugClass+"\n"
	
	#return HttpResponse(druglist)
	#return  render(request, 'searchedDrug.html', {'drugList': drugList})
	



#url="http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ"
# sp=spider(url)
# html=sp.getData()

# dictionlist=[ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
# removeDict=[ '0','1', '2', '3', '4', '5', '6', '7', '8', '9',"、"]
# tag="section"
# exdata=extractDrugs(html, tag, dictionlist)
# drugDict=exdata.getDrug()


# drugInterLabel=", "
# drugByNameLabelList=["（"," (",")","("]
# drugFm=drugFormer(drugDict, drugInterLabel, drugByNameLabelList,removeDict)
# drugList=drugFm.formDrug()


# drugclss=[]
# for each in drugList:
# 	print each.drugname+"		"+each.drugByname+"		"+each.drugClass
# 	if  each.drugClass  not in  drugclss:
# 		drugclss.append(each.drugClass )
# print len(drugclss)
