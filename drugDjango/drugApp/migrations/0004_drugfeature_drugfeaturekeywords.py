# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugApp', '0003_auto_20170911_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugfeature',
            name='drugFeatureKeyWords',
            field=models.TextField(default=None),
        ),
    ]
