# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-04 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
