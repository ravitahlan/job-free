import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from company.models import Job, CompanyModel

# Create your models here.

class UserModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user's personal information
    full_name = models.CharField(max_length = 60, blank = False)
    user_email = models.EmailField(null = True)
    gender_options = (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    gender = models.CharField(max_length = 6, choices = gender_options, default = 'Male')
    date_of_birth = models.DateField(null = True, blank = True)
    mobile_number = models.PositiveIntegerField()
    address_line1 = models.CharField(max_length = 100, blank = True)
    address_line2 = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 100, blank = False)
    state = models.CharField(max_length = 100, blank = False)
    zip = models.PositiveIntegerField()

    #user's educational information
    tenth_institution = models.CharField(max_length = 100, blank = True)
    tenth_board = models.CharField(max_length = 100, blank = True)
    tenth_result = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True)
    tenth_date = models.DateField(null = True, blank = True,default=datetime.date.today)

    twelfth_institution = models.CharField(max_length = 100, blank = True)
    twelfth_board = models.CharField(max_length = 100,null = True, blank = True)
    twelfth_result = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)
    twelfth_date = models.DateField(null = True, blank = True,default=datetime.date.today)

    diploma_institution = models.CharField(max_length = 100, blank = True,null = True)
    diploma_board = models.CharField(max_length = 100, blank = True,null = True)
    diploma_result = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True,null = True)
    diploma_date = models.DateField(null = True, blank = True,default=datetime.date.today)

    bachelor_institution = models.CharField(max_length = 100, blank = True)
    bachelor_board = models.CharField(max_length = 100, blank = True)
    bachelor_result = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True)
    bachelor_program = models.CharField(max_length = 100, blank = True)
    bachelor_stream = models.CharField(max_length = 100, blank = True)
    bachelor_date = models.DateField(null = True, blank = True,default=datetime.date.today)

    resume_headline = models.CharField(max_length = 500, blank = True, null = True)

    extra_curriculam = models.CharField(max_length = 600, blank = True,null = True)
    hobies = models.CharField(max_length = 600, blank = True,null = True,)


    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse(
            "job_seeker:detail",
            kwargs={
                "pk": self.pk
            }
        )
    # def get_absolute_url(self):
    #     return reverse('job_seeker:detail', kwargs = {'pk':self.pk})

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'skills')
    skill_name = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
        return reverse(
            "job_seeker:skill_detail",
            kwargs={
                "pk": self.pk
            }
        )

class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'projects')
    project_name = models.CharField(max_length = 100, blank = False)
    project_description = models.CharField(max_length = 600, blank = False)
    project_link = models.URLField(max_length = 500, blank = True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse(
            "job_seeker:project_detail",
            kwargs={
                "pk": self.pk
            }
        )

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'certifications')
    certification_name = models.CharField(max_length = 300, blank = False)
    certification_organization = models.CharField(max_length = 100, blank = False, null = True)
    certificate_link = models.URLField(max_length = 500, blank = True)
    valid_from = models.DateField()
    valid_till = models.DateField()

    def __str__(self):
        return self.certification_name

    def get_absolute_url(self):
        return reverse(
            "job_seeker:certification_detail",
            kwargs={
                "pk": self.pk
            }
        )

class Award(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'awards')
    award_name = models.CharField(max_length = 100, blank = False)
    award_organization = models.CharField(max_length = 200, blank = False)
    award_description = models.CharField(max_length = 600, blank = True)

    def __str__(self):
        return self.award_name + " by " + self.award_organization

    def get_absolute_url(self):
        return reverse(
            "job_seeker:award_detail",
            kwargs={
                "pk": self.pk
            }
        )


class Jobs(models.Model):
    company_user = models.ForeignKey(CompanyModel, on_delete = models.CASCADE, related_name = 'company_user')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "job_user")
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    applied_date = models.DateField(default=datetime.date.today)

    status = (
        ('Applied', 'Applied'),
        ('Reviewed', 'Reviewed'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected')
    )

    job_status = models.CharField(choices = status, max_length = 30, blank = False, null = False)

    def __str__(self):
        return self.job_status + ' in ' + self.company_user.company_name + ' for '+ self.job.job_profile + ' : Rs '+ str(self.job.salary)
