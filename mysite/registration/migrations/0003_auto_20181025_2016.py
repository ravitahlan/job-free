# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-25 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20181004_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]