# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0002_auto_20170904_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='code',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
    ]