# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-26 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0002_auto_20181026_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='bachelor_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='diploma_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='tenth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='twelfth_date',
            field=models.DateField(null=True),
        ),
    ]