# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
