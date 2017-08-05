# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  drug(models.Model):
    drugname = models.CharField(max_length=50)
    drugByname= models.CharField(max_length=50)
    drugClass=models.CharField(max_length=50)