
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug
from drugApp.models import drugFeature
from django.shortcuts import render
# 数据库操作
def  searchTumorUrl(request):
    # 初始化

    return  render(request, 'searchUrls.html')
    #return HttpResponse("<p>" + response + "</p>")

def  UseFulUrls(request):
    request.encoding='utf-8'
    url=request.GET['url']
    keyword=request.GET['keyword']
    

    drugList = drugFeature.objects.all()
    return  render(request, 'showDragInfo.html', {'drugList': drugList})
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1) 
    
  
    	
