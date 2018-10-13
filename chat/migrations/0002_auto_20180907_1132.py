# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-07 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
