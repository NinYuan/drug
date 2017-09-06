
# -*- coding: utf-8 -*-
 

from django.http import HttpResponse
 
from drugApp.models import drug,drugNames
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

