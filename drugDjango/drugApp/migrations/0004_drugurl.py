# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugApp', '0003_auto_20170905_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='drugUrl',
            fields=[
                ('drugUrl', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('UrlDescribe', models.CharField(max_length=100)),
            ],
        ),
    ]
