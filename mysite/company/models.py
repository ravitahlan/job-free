import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class CompanyModel(models.Model):
    user = models.ForeignKey(User, related_name='company_det',on_delete = models.CASCADE)

    company_name = models.CharField(max_length = 100, null = False, blank = False)
    company_field = models.CharField(max_length = 100, null = False, blank = False)
    comapany_country = models.CharField(max_length = 100, null = False, blank = False)
    company_email = models.EmailField(null = False, blank = True)
    company_contact = models.PositiveIntegerField(null = False, blank = False)
    company_website = models.URLField(null = True, blank = True)
    company_description = models.CharField(max_length = 400, blank = False, null = False)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse(
            "company:company_detail",
            kwargs={
                "pk": self.pk
            }
        )

class Job(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    profile_choices = (
        ('Business Development (Sales)', 'Business Development (Sales)'),
        ('Web Development', 'Web Development'),('Graphic Design','Graphic Design'),
        ('Content Writing','Content Writing'),('Operations','Operations'),('Mobile App Development','Mobile App Development'),
        ('Social Media Marketing','Social Media Marketing'),
        ('Marketing','Marketing'),('Digital Marketing','Digital Marketing'),
        ('Human Resources (HR)', 'Human Resources (HR)'),
        ('Law/ Legal', 'Law/ Legal'),('Campus Ambassador', 'Campus Ambassador')
        )
    type_choices = (
        ('Regular', 'Regular (In-office/On-field)'),
        ('Work From Home', 'Work From Home')
    )

    company_name = models.CharField(max_length = 100, null = True)
    company_website = models.URLField(null = True, blank = True)
    company_email = models.EmailField(null = True, blank = True)
    job_profile = models.CharField(max_length = 100, choices = profile_choices, null = False)
    job_type = models.CharField(max_length = 100, choices = type_choices, null = False)
    job_location = models.CharField(max_length = 100, null = False, blank = False)
    job_vacancy = models.PositiveIntegerField(null = True, blank = True)
    posted_date = models.DateField(default=datetime.date.today)
    date_from = models.DateField(null = False)
    date_till = models.DateField(null = False)
    job_description = models.CharField(max_length = 400, blank = False, null = False)
    salary = models.PositiveIntegerField(null = False, blank = False)
    perks = models.CharField(max_length = 300, blank = True, null = True)

    def __str__(self):
        return self.job_profile+ " : Rs" +str(self.salary)

    def get_absolute_url(self):
        return reverse(
            "company:job_detail",
            kwargs={
                "pk": self.pk
            }
        )
