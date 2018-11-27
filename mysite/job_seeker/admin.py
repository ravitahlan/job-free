from django.contrib import admin
from job_seeker.models import UserModel, Skill, Project, Certification, Award, Jobs
# Register your models here.

admin.site.register(UserModel)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Award)
admin.site.register(Certification)
admin.site.register(Jobs)
