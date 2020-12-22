# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-22 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
