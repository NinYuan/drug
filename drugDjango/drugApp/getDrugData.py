
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse

from drugApp.models import drug,drugNames
from drugApp.models import drugFeature
# from drugApp.models import *
from django.shortcuts import render

from drugApp.dbDataProc.getFeature import drugFeaturer
from drugApp.Tools.typeTrans import dictString

# from drugApp.drugClass.DrugStruc import dFeature
from drugApp.drugClass.DrugStruc import *

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import HttpResponse
from django.shortcuts import render
import json

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]







# 数据库操作
def  getDrug(request):
    # 初始化
  
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    drugList = drug.objects.all()
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1) 
    
  
    return  render(request, 'showDrug.html', {'drugList': drugList})
    #return HttpResponse("<p>" + response + "</p>")

def  getDrugBaike(request):
    drugList = drugFeature.objects.all()
    # for each in drugList:
    #     print each
    #     return HttpResponse("<p>" + "ok" + "</p>")
    return  render(request, 'showDragInfo.html', {'drugList': drugList})



def  getDrugName(request):
    drugList = drugNames.objects.all()
    
    return  render(request, 'showGeneralDrug.html', {'drugList': drugList})
        
    # # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = drug.objects.filter(drugname=1) 
    
def EchartDrugInfo(request):
    drugList = drugFeature.objects.all()
    allDrugFeature = drugFeaturer()
    featurers=allDrugFeature.getFeature(drugList)
    dstr=dictString()
    reFeature=[]
    

    for each in featurers:
        if each.featureNum>1:

            reFeature.append(each)

    
    return  render(request, 'showFeatureInfo.html', {'drugList': reFeature})

def getEchart(request):


    feature=request.GET['feature']

    featureNum=request.GET['featureNum']
    drugs=request.GET['drugs']
    subfeaturesstr=request.GET['subfeatures']
    subfeature=subfeaturesstr.split(" ")
    for each in subfeature:
        if each=="":
            subfeature.remove("")
    featuredict={}
    drugList = drugFeature.objects.all()
    featurelists=[]
    dfs=[]
    for edrug in drugList:
        
        kws=edrug.drugFeatureKeyWords.split(",")
        for ekw in kws:

            if ekw  in subfeature:
                if ekw not in featurelists:
                    
                    drugl=[edrug.drugname]
                    df=dFeature(ekw, 1, drugl, "")
                    dfs.append(df)
                    featurelists.append(ekw)
                else:
                    for  edf in dfs:
                        if ekw ==edf.feature:
                            edf.featureNum+=1
                            edf.drugs.append(edrug.drugname)
    
    featureDrug={}
    featureNumDict={}
    rfn=""
    rfd=""
    for  edf in dfs:
        #rfd+=str(edf.featureNum)+":"+"\n".join(edf.drugs)+"*"+edf.feature+"#"
        rfd+=str(edf.featureNum)+":"+edf.feature+"*"+"\n".join(edf.drugs)+"#"
       
       
      
        
    return render(request, 'Pie.html', {
         'featureDrug': json.dumps(rfd),
        # 'featureNumDict': json.dumps(rfn),
     })



def showDrugs(request):


    feature=request.GET['feature']
    drugList = drugFeature.objects.all()
    # return HttpResponse("<p>" + feature + "</p>")
    # featureNum=request.GET['featureNum']
    # drugs=request.GET['drugs']
    # subfeaturesstr=request.GET['subfeatures']
    # subfeature=subfeaturesstr.split(" ")
    # for each in subfeature:
    #     if each=="":
    #         subfeature.remove("")
    # featuredict={}
    # drugList = drugFeature.objects.all()
    # featurelists=[]
    # dfs=[]
    drugnames=[]
    for edrug in drugList:
        
        kws=edrug.drugFeatureKeyWords.split(",")
        for ekw in kws:
            if ekw==feature:
                if edrug.drugname not in drugnames:
                    drugnames.append(edrug.drugname)

    return  render(request, 'showMainDrugs.html', {'drugnames': drugnames})

def getDrugInfo(request):


    eachdrug=request.GET['drugname']
    drugList = drugFeature.objects.all()
    
    drugnames=[]
    rdict=[]
    for edrug in drugList:
        if edrug.drugname==eachdrug:
            print edrug.featureName
            edf=drugFeature(drugname="",featureName=edrug.featureName,drugFeatureContent=edrug.drugFeatureContent,drugFeatureKeyWords="")
            rdict.append(edf)
            #rdict[edrug.featureName]=edrug.drugFeatureContent



        # kws=edrug.drugFeatureKeyWords.split(",")
        # for ekw in kws:
        #     if ekw==feature:
        #         if edrug.drugname not in drugnames:
        #             drugnames.append(edrug.drugname)

    return  render(request, 'showInfo.html', {'drugname': eachdrug,"Info":rdict},)

   