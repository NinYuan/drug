
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug
from drugApp.models import drugFeature,drugUrl
from django.shortcuts import render
# 数据库操作
def  manuDrug(request):
    # 初始化
  
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    drugList = drug.objects.all()
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1) 
    
  

    return  render(request, 'manageDrug.html')
    #return HttpResponse("<p>" + response + "</p>")

def  ProcDelDrug(request):
    drug.objects.delete()
    return HttpResponse("<p>数据删除成功！</p>") 


def  showDrugUrl(request):
    drugList = drugUrl.objects.all()
    return  render(request, 'showDrugUrl.html', {'drugList': drugList})

def  addDrugUrl(request):
    request.encoding='utf-8'
    #url="http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ"

    Url=request.GET['drugUrl']
    UrlDesc=request.GET['UrlDescribe']
    TumorUrl=drugUrl(drugUrl=Url,UrlDescribe=UrlDesc)
    TumorUrl.save()
   
    return HttpResponse("<p>Url Add成功！</p>") 
    
  
    	
