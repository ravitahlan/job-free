# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-21 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0014_auto_20181122_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='company_user',
        ),
    ]
