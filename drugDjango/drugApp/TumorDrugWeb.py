
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug,drugNames
from drugApp.models import drugFeature
from django.shortcuts import render
# 数据库操作
def  MainEntry(request):
    # 初始化
  
   return  render(request, 'MainDrug.html')
    #return HttpResponse("<p>" + response + "</p>")

