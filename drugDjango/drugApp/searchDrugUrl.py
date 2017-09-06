
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug
from drugApp.models import drugFeature
from django.shortcuts import render
from drugApp.getData.getDrugsInt import *
from drugApp.ProcData.extractDrugName import extractDrugs
import os
# 数据库操作
def  searchTumorUrl(request):
    # 初始化

    return  render(request, 'searchUrls.html')
    #return HttpResponse("<p>" + response + "</p>")

# def  UseFulUrls(request):
#     request.encoding='utf-8'
#     url=request.GET['url']
#     keyword=request.GET['keyword']
    
#     newUrl=url+
#     drugList = drugFeature.objects.all()
#     return  render(request, 'showDragInfo.html', {'drugList': drugList})
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1)  
def  procDrugName(request):
    request.encoding='utf-8'
    durl=request.GET['url']
    dlocalpostion=request.GET['localpostion']
    dpostion=request.GET['postion']
    ddvision=request.GET['divisioin']
    

    # sp=spider(durl)
    # html=sp.getData()
    # return HttpResponse(html)

    #file="/home/hong/桌面/大四医疗信息系统设计/[菩提众生]抗肿瘤药大全.html"
    html=open(dlocalpostion).read()
    #return HttpResponse(html)
    # file="/home/hong/桌面/大四医疗信息系统设计/[菩提众生]抗肿瘤药大全.html"
    # html=open(file).read()
    # tag="p"
    # pattern='[（|、|）|其中|的]'
    exdata=extractDrugs(html, dpostion)
    drugNameText=exdata.getDrug(ddvision)
    for drug in drugNameText:
        if drug=='\n':
            drugNameText.remove('\n')
        if drug=='':
            drugNameText.remove('')
        if drug=="":
            drugNameText.remove("")
        if drug==" ":
            drugNameText.remove("\n\r")

    #drugNameText.remove()

    #message=""
    # exdata=extractDrugs(html, dpostion, ddvision)
    # drugDict=exdata.getDrug()
   # os.remove(dlocalpostion)
    #drug="***".join(drugNameText)


    return  render(request, 'generalSearchedDrugName.html', {'drugNameText': drugNameText})

    # return HttpResponse(drug)
    # drugList = drugFeature.objects.all()
    # return  render(request, 'showDragInfo.html', {'drugList': drugList})
  
    	
