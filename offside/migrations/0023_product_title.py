# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offside', '0022_news_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
