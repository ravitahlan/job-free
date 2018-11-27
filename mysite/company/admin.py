from django.contrib import admin
from company.models import CompanyModel, Job
# Register your models here.

admin.site.register(CompanyModel)
admin.site.register(Job)
