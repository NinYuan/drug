"""drugDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from drugApp import views
from drugApp import downDrug,getBaikeFeature
from drugApp import getDrugData,tumorDrug,drugBaikeFeature,searchDrugUrl,TumorDrugWeb
from drugApp import manageDrug
from drugApp import LineChartJSONView,tes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^down$', downDrug.down),
    url(r'^getdrug$',getDrugData.getDrug),
    url(r'^search-drug$', tumorDrug.search_drug),
    url(r'^search$', tumorDrug.search),
    url(r'^search-drugBaikeFeature$', drugBaikeFeature.searchBaikeFeature),
    url(r'^show-drugBaikeFeature$', getDrugData.getDrugBaike),

    url(r'^manage-drug$', manageDrug.manuDrug),
    url(r'^delete-procDrug$', manageDrug.ProcDelDrugName),
    url(r'^add-procDrugUrl$', manageDrug.addDrugUrl),

    url(r'^search-drugUrls$', searchDrugUrl.searchTumorUrl),
    
    url(r'^search-procDrugName$', searchDrugUrl.procDrugName),

     url(r'^downDrug$', downDrug.downDrugName),
     url(r'^getgeneraldrug$',getDrugData.getDrugName),

     url(r'^TumorDrug$', TumorDrugWeb.MainEntry),

     url(r'^show-DrugUrl$', manageDrug.showDrugUrl),

     url(r'^delete-procLocalUrl$', manageDrug.ProcDelLocalUrl),

     url(r'^downAllDrug$', downDrug.downAllDrug),

     # url(r'^echartLines$', LineChartJSONView.echartLines),
     # url(r'^line_chart_json$', LineChartJSONView.testLine),

     url(r'^EchartDrugInfo$', getDrugData.EchartDrugInfo),
     url(r'^getEchart$', getDrugData.getEchart),
     url(r'^showDrugs$', getDrugData.showDrugs),
     url(r'^getDrugInfo$', getDrugData.getDrugInfo),

     #EchartDrugInfo

     url(r'^line_chart/$', LineChartJSONView.line_chart,
        name='line_chart'),
    url(r'^line_chart/json/$', LineChartJSONView.line_chart_json,
        name='line_chart_json'),

    url(r'^todb$', tes.chance),
    url(r'^getKeyWord$', getBaikeFeature.chance),
    
    

]



