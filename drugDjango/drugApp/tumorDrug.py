# -*- coding: utf-8 -*-

 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from drugApp.ProcData.extractData import *
from drugApp.drugClass.formDrugs import *
from drugApp.drugClass.formElem import *
from drugApp.getData.getDrugsInt import *

def search_drug(request):
	
	elemList=formElm()
	
	return render(request, 'searchDrug.html', {'elemList': elemList})
    #return render_to_response('searchDrug.html')
 
# 接收请求数据
def search(request):  
	request.encoding='utf-8'
	#url="http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ"
	url=request.GET['url']
	sp=spider(url)
	html=sp.getData()
	# dictionlist=[ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
	getdictionlist=request.GET['dictionlist']
	dictionlist=
	#removeDict=[ '0','1', '2', '3', '4', '5', '6', '7', '8', '9',"、"]
	removeDict=request.GET['removeDict']
	#tag=""
	tag=request.GET['tag']
	#drugInterLabel=", "
	drugInterLabel=request.GET['drugInterLabel']
	#drugByNameLabelList=["（"," (",")","("]
	drugByNameLabelList=request.GET['drugByNameLabelList']

	exdata=extractDrugs(html, tag, dictionlist)
	drugDict=exdata.getDrug()
	drugFm=drugFormer(drugDict, drugInterLabel, drugByNameLabelList,removeDict)
	drugList=drugFm.formDrug()

	return  render(request, 'searchedDrug.html', {'drugList': drugList})
	#return HttpResponse(message)

	# if 'q' in request.GET:
	# 	message = 'you seartch: ' + request.GET['q']
	# else:
 #       		 message = '你提交了空表单'
    



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
