# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-20 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wheel',
            name='isDelete',
        ),
    ]
