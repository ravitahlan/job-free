# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-13 14:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='comapany_country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_detail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_profile',
            field=models.CharField(choices=[('Business Development (Sales)', 'Business Development (Sales)'), ('Web Development', 'Web Development'), ('Graphic Design', 'Graphic Design'), ('Content Writing', 'Content Writing'), ('Mobile App Development', 'Mobile App Development'), ('Operations', 'Operations'), ('Social Media Marketing', 'Social Media Marketing'), ('Marketing', 'Marketing'), ('Digital Marketing', 'Digital Marketing'), ('Human Resources (HR)', 'Human Resources (HR)'), ('Law/ Legal', 'Law/ Legal'), ('Campus Ambassador', 'Campus Ambassador')], max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Regular', 'Regular (In-office/On-field)'), ('Work From Home', 'Work From Home')], max_length=100),
        ),
    ]