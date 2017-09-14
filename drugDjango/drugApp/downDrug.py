
# -*- coding: utf-8 -*-
 

from django.http import HttpResponse
 
from drugApp.models import drug,drugNames,AlldrugNames
from django.shortcuts import render
# 数据库操作
def  down(request):
	request.encoding='utf-8'

	drugClasslist =  request.GET.getlist('drugClass')
	drugnamelist =  request.GET.getlist('drugname')
	drugBynamelist =  request.GET.getlist('drugByname')
	for i in range(len(drugClasslist)):

		edrugname=drugnamelist[i]
		if  edrugname=="None":
			continue
		try:
			response = drug.objects.get(drugname=edrugname) 
			continue
		except Exception as e:
			pass
		
		edrugByName=drugBynamelist[i]
		edrugClass=drugClasslist[i]
		eachDrug=drug(drugname=edrugname, drugByname=edrugByName, drugClass=edrugClass)
		eachDrug.save()

	context={}
    	context['para']="drugNames数据添加成功！"
    	return  render(request, 'mysqlResult.html',context)
	#return HttpResponse("<p>数据添加成功！</p>")

def  downDrugName(request):
	request.encoding='utf-8'

	
	drugnamelist =  request.GET.getlist('drugname')
	
	for i in range(len(drugnamelist)):

		edrugname=drugnamelist[i]
		if  edrugname=="None":
			continue
		if edrugname=="":
			continue
		try:
			response = drugNames.objects.get(drugname=edrugname) 
			continue
		except Exception as e:
			pass
		
		eachDrug=drugNames(drugname=edrugname)
		eachDrug.save()
	context={}
    	context['para']="drugNames数据添加成功！"
    	return  render(request, 'mysqlResult.html',context)
	#return HttpResponse("<p>数据添加成功！</p>")

	# message=drugClass+drugname+drugByname
	# print "down
	# print drugClass
	#  drug1=drug(drugname="2",drugByname="2",drugClass="3")
	# drug1.save()
	#return HttpResponse("<p>数据添加成功！</p>")

	AlldrugNames
	drugname= models.CharField(max_length=100)
	drugArticle= models.CharField(max_length=100)
	drugKnowledgeRef= models.CharField(max_length=100)

def downAllDrug(request):
	newdrugname =  request.GET.getlist('newdrugname')
	alreadydrugname =  request.GET.getlist('alreadydrugname')
	cantdrugname =  request.GET.getlist('cantdrugname')
	#durl =  request.GET.getlist('durl')
	durl =  request.GET['drugurl']
	#return HttpResponse(durl)
	#durl =  request.GET['durl']
	# dnew=len(newdrugname)
	# dalready=len(alreadydrugname)
	# return HttpResponse(dnew+"***"+dalready) 
	 
	drugList=[]
	for i in range(len(newdrugname)):
		edrugnamelist=newdrugname[i]+alreadydrugname[i]+cantdrugname[i]
		if cantdrugname!="":
			edrugKnow="Baidu"
		else:
			edrugKnow=""

		eachDrug=AlldrugNames(drugname=edrugnamelist, drugArticle=durl, drugKnowledgeRef=edrugKnow)
		#drugList.append(eachDrug)
		#return HttpResponse(edrugnamelist+"*"+durl+"*"+edrugKnow)
		try:
			eachDrug.save()
		except Exception as e:
			pass
		

	#drugList = AlldrugNames.objects.all()
	context={}
    	context['para']="all drugName 数据添加成功！"
    	return  render(request, 'mysqlResult.html',context)
    	
    	#return  render(request, 'showAllDrug.html', {'drugList': drugList})
	# pass
