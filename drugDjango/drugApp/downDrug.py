
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from drugApp.models import drug
 
# 数据库操作
def  down(request):
	data =  request.GET['data']
	drug1=drug(drugname="2",drugByname="2",drugClass="3")
	drug1.save()
	return HttpResponse("<p>数据添加成功！</p>")
