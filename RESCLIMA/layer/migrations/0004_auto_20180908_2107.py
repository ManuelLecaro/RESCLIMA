# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layer', '0003_auto_20180908_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layer',
            old_name='ts_vector',
            new_name='textsearchable_index',
        ),
    ]
