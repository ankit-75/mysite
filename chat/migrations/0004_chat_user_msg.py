# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-07 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_roomname'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='user_msg',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
