# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-15 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zjapp', '0002_auto_20180515_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='zjapp.CategoryModel'),
        ),
    ]