# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-18 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_chat_id_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_id',
            name='channel_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
