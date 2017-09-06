
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug
from drugApp.models import drugFeature
from django.shortcuts import render
# 数据库操作
def  getDrug(request):
    # 初始化
  
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    drugList = drug.objects.all()
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1) 
    
  
    return  render(request, 'showDrug.html', {'drugList': drugList})
    #return HttpResponse("<p>" + response + "</p>")

def  getDrugInfo(request):
	drugList = drugFeature.objects.all()
	return  render(request, 'showDragInfo.html', {'drugList': drugList})
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1) 
    
  
    	
