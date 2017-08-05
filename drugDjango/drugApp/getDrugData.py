
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug
 
# 数据库操作
def  getDrug(request):
    # 初始化
    response = ""
    response1 = ""
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = drug.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = drug.objects.filter(drugname=1) 
    
    # 获取单个对象
    #response3 = drug.objects.get(drugname=1) 

    for var in response2:
        response1 += var.drugname + " ok"
    # 输出所有数据
    # for var in list:
           #response1 += var.drugname + " ok"
    response = response1
    return HttpResponse("<p>" + response + "</p>")
