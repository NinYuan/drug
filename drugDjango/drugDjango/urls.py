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
from drugApp import downDrug
from drugApp import getDrugData,tumorDrug,drugBaikeFeature,searchDrugUrl
from drugApp import manageDrug

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^down$', downDrug.down),
    url(r'^getdrug$',getDrugData.getDrug),
    url(r'^search-drug$', tumorDrug.search_drug),
    url(r'^search$', tumorDrug.search),
    url(r'^search-drugBaikeFeature$', drugBaikeFeature.searchBaikeFeature),
    url(r'^show-drugBaikeFeature$', getDrugData.getDrugInfo),

    url(r'^manage-drug$', manageDrug.manuDrug),
    url(r'^delete-procDrug$', manageDrug.ProcDelDrug),
    url(r'^add-procDrugUrl$', manageDrug.addDrugUrl),

    url(r'^search-drugUrls$', searchDrugUrl.searchTumorUrl),
    url(r'^search-procUrls$', searchDrugUrl.UseFulUrls),
]



