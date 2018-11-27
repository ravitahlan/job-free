# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-25 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=100)),
                ('award_organization', models.CharField(max_length=200)),
                ('award_description', models.CharField(blank=True, max_length=600)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(max_length=300)),
                ('certificate_link', models.URLField(blank=True, max_length=500)),
                ('valid_from', models.DateField()),
                ('valid_till', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.CharField(max_length=600)),
                ('project_link', models.URLField(blank=True, max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=6)),
                ('date_of_birth', models.DateField()),
                ('mobile_number', models.PositiveIntegerField()),
                ('address_line1', models.CharField(blank=True, max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.PositiveIntegerField()),
                ('tenth_institution', models.CharField(blank=True, max_length=100)),
                ('tenth_board', models.CharField(blank=True, max_length=100)),
                ('tenth_result', models.DecimalField(decimal_places=2, max_digits=5)),
                ('twelfth_institution', models.CharField(blank=True, max_length=100)),
                ('twelfth_board', models.CharField(blank=True, max_length=100)),
                ('twelfth_result', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diploma_institution', models.CharField(blank=True, max_length=100)),
                ('diploma_board', models.CharField(blank=True, max_length=100)),
                ('diploma_result', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bachelor_institution', models.CharField(blank=True, max_length=100)),
                ('bachelor_board', models.CharField(blank=True, max_length=100)),
                ('bachelor_result', models.DecimalField(decimal_places=2, max_digits=5)),
                ('resume_headline', models.CharField(blank=True, max_length=500)),
                ('extra_curriculam', models.CharField(blank=True, max_length=600)),
                ('hobies', models.CharField(blank=True, max_length=600)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
