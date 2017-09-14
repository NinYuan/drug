# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  drug(models.Model):
    drugname = models.CharField(max_length=100)
    drugByname= models.CharField(max_length=100)
    drugClass=models.CharField(max_length=100)

class drugFeature(models.Model):
	"""docstring for drugFeature"""
	drugname = models.CharField(max_length=100)
	featureName= models.CharField(max_length=100)
	drugFeatureContent=models.TextField()
	drugFeatureKeyWords=models.TextField(default=None)
	#drugFeature=models.CharField(max_length=3000)

class  drugUrl(models.Model):
    drugUrl= models.CharField(max_length=100,primary_key=True)
    UrlDescribe=models.CharField(max_length=100)

#store drug name
class drugNames(models.Model):
	drugname= models.CharField(max_length=100,primary_key=True)


#all drugNames Get From Internet
class AlldrugNames(models.Model):
	drugname= models.CharField(max_length=200)
	drugArticle= models.CharField(max_length=200)
	drugKnowledgeRef= models.CharField(max_length=200)

	class Meta:
	        #db_table = 'drugApp_alldrugnames'
	        unique_together = ("drugname", "drugArticle") 
								