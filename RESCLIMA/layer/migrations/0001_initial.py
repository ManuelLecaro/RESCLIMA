# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 15:24
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_index', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
                ('categories_string', models.TextField(blank=True, max_length=600, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('abstract', models.TextField(max_length=500, null=True)),
                ('type', models.CharField(max_length=10)),
                ('data_date', models.DateField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('srs_wkt', models.TextField(max_length=500)),
                ('bbox', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
