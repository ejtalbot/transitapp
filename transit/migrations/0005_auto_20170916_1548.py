# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0004_line_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line',
            old_name='code',
            new_name='color',
        ),
    ]
