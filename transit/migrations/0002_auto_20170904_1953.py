# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='name',
            field=models.CharField(choices=[('GR', 'Green'), ('BL', 'Blue'), ('SV', 'Silver'), ('RD', 'Red'), ('OR', 'Orange'), ('YL', 'Yellow')], max_length=2, unique=True),
        ),
    ]
