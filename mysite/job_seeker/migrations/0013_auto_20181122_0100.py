# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-21 19:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0012_auto_20181122_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='company_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Job'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_user', to=settings.AUTH_USER_MODEL),
        ),
    ]