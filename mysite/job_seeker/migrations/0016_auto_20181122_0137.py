# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-21 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0015_remove_jobs_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='user',
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]