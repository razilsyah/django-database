# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-29 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.CharField(choices=[('jurnal', 'jurnal'), ('berita', 'berita'), ('blog', 'blog')], default='blog', max_length=20),
        ),
    ]
